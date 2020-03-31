from contextlib import contextmanager
from pathlib import Path
from subprocess import Popen
from typing import Optional

# TODO decorator that records a video if a certain env var/flag is set (pass a custom name too)

@contextmanager
def hotkeys(geometry: Optional[str]=None):
    # TODO kill in advance??
    ctx = Popen([
        'screenkey',
        '--no-detach',
        '--timeout', '2',
        '--key-mode', 'composed',
        '--font-size', 'large',
        # TODO font color?
        *([] if geometry is None else ['-g', geometry]),
    ])
    with ctx as p:
        try:
            yield p
        finally:
            p.kill()


@contextmanager
def record(output: Optional[Path]=None, wid: Optional[str]=None, quality: Optional[str]=None):
    assert output is not None, "TODO use tmp file or current dir??"

    # TODO I think recordmydesktop dumps broken file. it's squeezed by ffmpeg somehow
    # also there is something about broken frames???

    ctx = Popen([
        'recordmydesktop',
        *([] if wid     is None else ['--windowid' , wid]),
        *([] if quality is None else ['--v_quality', quality]),

        '--no-sound',
        '--on-the-fly-encoding',
        '--workdir=/tmp', # TODO not sure..

        '--overwrite', # TODO make optional?
        '--output', output,
    ])
    with ctx as p:
        try:
            yield p
        finally:
            # TODO check if it terminated gracefully?
            p.terminate()
            p.wait(timeout=10)


# https://stackoverflow.com/a/52669454/706389
CURSOR_SCRIPT = '''
function enableCursor() {
  var seleniumFollowerImg = document.createElement("img");
  seleniumFollowerImg.setAttribute('src', 'data:image/png;base64,'
    + 'iVBORw0KGgoAAAANSUhEUgAAABQAAAAeCAQAAACGG/bgAAAAAmJLR0QA/4ePzL8AAAAJcEhZcwAA'
    + 'HsYAAB7GAZEt8iwAAAAHdElNRQfgAwgMIwdxU/i7AAABZklEQVQ4y43TsU4UURSH8W+XmYwkS2I0'
    + '9CRKpKGhsvIJjG9giQmliHFZlkUIGnEF7KTiCagpsYHWhoTQaiUUxLixYZb5KAAZZhbunu7O/PKf'
    + 'e+fcA+/pqwb4DuximEqXhT4iI8dMpBWEsWsuGYdpZFttiLSSgTvhZ1W/SvfO1CvYdV1kPghV68a3'
    + '0zzUWZH5pBqEui7dnqlFmLoq0gxC1XfGZdoLal2kea8ahLoqKXNAJQBT2yJzwUTVt0bS6ANqy1ga'
    + 'VCEq/oVTtjji4hQVhhnlYBH4WIJV9vlkXLm+10R8oJb79Jl1j9UdazJRGpkrmNkSF9SOz2T71s7M'
    + 'SIfD2lmmfjGSRz3hK8l4w1P+bah/HJLN0sys2JSMZQB+jKo6KSc8vLlLn5ikzF4268Wg2+pPOWW6'
    + 'ONcpr3PrXy9VfS473M/D7H+TLmrqsXtOGctvxvMv2oVNP+Av0uHbzbxyJaywyUjx8TlnPY2YxqkD'
    + 'dAAAAABJRU5ErkJggg==');
  seleniumFollowerImg.setAttribute('id', 'selenium_mouse_follower');
  seleniumFollowerImg.setAttribute('style', 'position: absolute; z-index: 99999999999; pointer-events: none; left:0; top:0');
  document.body.appendChild(seleniumFollowerImg);
  document.onmousemove = function (e) {
    document.getElementById("selenium_mouse_follower").style.left = e.pageX + 'px';
    document.getElementById("selenium_mouse_follower").style.top  = e.pageY + 'px';
  };
};

enableCursor();
'''


# https://stackoverflow.com/a/987376/706389
SELECT_SCRIPT = '''
function selectText(node) {
    if (document.body.createTextRange) {
        const range = document.body.createTextRange();
        range.moveToElementText(node);
        range.select();
    } else if (window.getSelection) {
        const selection = window.getSelection();
        const range = document.createRange();
        range.selectNodeContents(node);
        selection.removeAllRanges();
        selection.addRange(range);
    } else {
        console.warn("Could not select text in node: Unsupported browser.");
    }
}
'''
