import os, time

def singleAlarmSound():
    duration = 0.35  # seconds
    # freq = 130  # Hz

    freqs = [100,130]
    for freq in freqs:
        os.system('play -nq -t alsa synth {} sine {}'.format(duration, freq))

def doubleAlarmSound():
    for i in range(0,2):
        duration = 0.35  # seconds
        # freq = 130  # Hz

        freqs = [100,130]
        for freq in freqs:
            os.system('play -nq -t alsa synth {} sine {}'.format(duration, freq))

        time.sleep(0.25)