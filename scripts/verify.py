"""Run finite supplementary checks; never represents them as an all-length proof."""
from pathlib import Path
import argparse,json,re,subprocess,sys,tempfile
ROOT=Path(__file__).resolve().parents[1]
ap=argparse.ArgumentParser();ap.add_argument('--lean',help='path to Lean 4.34.1');args=ap.parse_args()
logs=ROOT/'verification/current';logs.mkdir(parents=True,exist_ok=True)
p=subprocess.run([sys.executable,str(ROOT/'verification/independent_checks.py')],stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
(logs/'independent-checks.json').write_bytes(p.stdout)
if p.returncode:raise SystemExit(p.stdout.decode(errors='replace'))
assert json.loads(p.stdout)['status']=='PASS'
print('Independent exact geometric checks: PASS')
if args.lean:
    version=subprocess.check_output([args.lean,'--version'],text=True)
    assert 'version 4.34.1' in version,version
    with tempfile.TemporaryDirectory(prefix='lean-finite-',dir=logs) as tmp:
        assert Path(tmp).resolve().is_relative_to(logs.resolve())
        p=subprocess.run([args.lean,'-j2','-o',str(Path(tmp)/'LatticePaths.olean'),'LatticePaths.lean'],
            cwd=ROOT/'verification/original/lean',stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
        (logs/'lean-kernel.txt').write_bytes(p.stdout)
        if p.returncode:raise SystemExit(p.stdout.decode(errors='replace'))
    text=p.stdout.decode(errors='replace')
    assert 'sorryAx' not in text and 'error:' not in text and 'native_decide' not in text
    found=re.findall(r"^'(\S+)' (does not depend on any axioms|depends on axioms: \[([^\]]*)\])",text,re.M)
    assert len(found)==7,found
    for name,_,axioms in found:assert {x.strip() for x in axioms.split(',') if x.strip()}<={'propext'},name
    (logs/'lean-axiom-audit.json').write_text(json.dumps({'version':version.strip(),'finite_theorems':7,'allowed_axioms':['propext'],'native_evaluation_axioms':False,'all_length_theorem_formalized':False,'status':'PASS'},indent=2))
    print('Seven bounded Lean kernel checks and axiom audit: PASS')
