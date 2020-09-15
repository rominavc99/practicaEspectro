import sys
sys.path.insert( 1, 'dps-modulo')

from thinkdsp import SinSignal
from thinkdsp import decorate
import thinkplot

senalUno = SinSignal(freq=380, amp=0.1, offset=0)
senalDos = SinSignal(freq=750, amp=1, offset =0)

mezcla = senalUno + senalDos

waveMezcla = mezcla.make_wave(duration=2, start=0,framerate=44100)
waveMezcla.plot()
decorate(xlabel = "tiempo")
thinkplot.show()

espectro = waveMezcla.make_spectrum()
espectro.plot()
decorate(xlabel="frecuencia hz")
thinkplot.show()