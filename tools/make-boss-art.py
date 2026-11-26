# Gera js/boss-art.js a partir de images/boss/*.png  (rode na pasta do jogo: python3 tools/make-boss-art.py)
import base64, glob, hashlib, json
files = sorted(glob.glob('images/boss/*.png'))
blobs, m = {}, {}
for f in files:
    b = open(f, 'rb').read(); h = hashlib.md5(b).hexdigest()
    blobs.setdefault(h, 'data:image/png;base64,' + base64.b64encode(b).decode()); m[f] = h
src = open('js/boss-art.js', encoding='utf-8').read() if False else None
head = '''/* boss-art.js (GERADO por tools/make-boss-art.py) - imagens dos bosses embutidas no código. */
var bossArt = (function() {
    var DATA = %s;
    var MAP = %s;
    return { get: function(path) { var h = MAP[path]; return h ? DATA[h] : path; } };
})();
'''
open('js/boss-art.js', 'w').write(head % (json.dumps(blobs), json.dumps(m)))
print('ok', len(blobs), 'imagens')
