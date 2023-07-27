import numpy as np
import random
import os

class FakeMSI():
    base_path = os.path.dirname(os.path.realpath(__file__))
    data_file_path = os.path.join(base_path, 'philData.npz')

    real_shot = np.load(data_file_path)['shot']



    def generate_shot(self):
        fake_shot = self.real_shot.copy()
        fake_shot['discharge_current'] *= (1 + np.random.normal(scale=0.1, size=(4096)))
        fake_shot['discharge_voltage'] *= (1 + np.random.normal(scale=0.1, size=(4096)))
        fake_shot['RGA_partials'] *= (1 + np.random.normal(scale=0.1, size=(50)))
        fake_shot['diode_signals'] *= (1 + np.random.normal(scale=0.1, size=(3, 4096)))
        fake_shot['datarun_shotnum'] += np.random.randint(0, 10000, dtype='uint32')
        fake_shot['datarun_key'] = np.char.add(fake_shot['datarun_key'], np.bytes_(''.join((' - ', *(chr(random.randrange(97, 97 + 26)) for i in range(10)))))).astype('|S128')
        fake_shot['interferometer_signals'] *= (1 + np.random.normal(scale=0.1, size=(1, 4096)))
        fake_shot['magnet_profile'] *= (1 + np.random.normal(scale=0.1, size=(1024)))
        fake_shot['pressure_fill'] *= (1 + np.random.normal(scale=0.1))
        fake_shot['spectrometer'][1] *= (1 + np.random.normal(scale=0.1, size=(3648)))
        return fake_shot


if __name__ == '__main__':
    print(FakeMSI.generate_shot(FakeMSI)['datarun_key'])
    print(FakeMSI.generate_shot(FakeMSI).dtype)
