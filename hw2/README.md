# HW2: Gábor transforms: Time-frequency analysis and music score extraction

Homework problem available at
https://faculty.washington.edu/kutz/582hw2.pdf

## Preview

### Part 1: Time-frequency analysis of Handel's music

Handel's music | FFT | Spectrogram by Gábor transform
:-------------------------:|:-------------------------:|:-------------------------:
![handelamp](https://github.com/yeewantung/AMATH-582/blob/master/hw2/images/handelamp.png)   | ![handelfreq](https://github.com/yeewantung/AMATH-582/blob/master/hw2/images/handelfreq.png) | ![gaussian](https://github.com/yeewantung/AMATH-582/blob/master/hw2/images/gaussian.png)

### Part 2: Music score extraction of *Mary had a little lamp*

Music piece          | Overtones of Piano | Spectrogram by Gábor transform
:-------------------------:|:-------------------------:|:-------------------------:
![music1amp](https://github.com/yeewantung/AMATH-582/blob/master/hw2/images/music1amp.png) | ![music1overtone](https://github.com/yeewantung/AMATH-582/blob/master/hw2/images/music1overtone.png) | ![music1spec](https://github.com/yeewantung/AMATH-582/blob/master/hw2/images/music1spec.png)

Music score extracted! (Plot created by LilyPond)
![music1score](https://github.com/yeewantung/AMATH-582/blob/master/hw2/images/music1score.png)

# Specification on files
* Report
  - [hw2.pdf](https://github.com/yeewantung/AMATH-582/blob/master/hw2/hw2.pdf): Report on the project
* Source code
  - [hw2.ipynb](https://github.com/yeewantung/AMATH-582/blob/master/hw2/hw2.ipynb): Jupyter notebook version of the code
* Datasets
  - Fs.npy, y.npy, handel.mat: 9 second piece of Handel's music
  - music1.wav, music2.wav: **Mary had a little lamp** played by piano and recorder
* Images and graphs
  - handelamp.png: Amplitude versus time plot of Handel's music
  - handelfreq.png: Fourier transform of Handel's music
  - gaussian1.png, mexican1.png, shannon1.png: Illustration of Gaussian function, Mexican hat function, Shannon step-like function
  - gaussian.png, gaussiansmall.png, gaussiansmall001.png, gaussianwide.png: Spectrograms of Handel's music by the Gábor transform with Gaussian window
  - mexican.png, mexicansmall.png, mexicansmall001.png, mexicanwide.png: Spectrograms of Handel's music by the Gábor transform with Mexican hat window
  - shannon.png, shannonsmall.png, shannonsmall001.png, shannonwide.png: Spectrograms of Handel's music by the Gábor transform with Shannon window
  - music1amp.png, music2amp.png: Amplitude versus time plot of **Mary had a little lamp** played by piano and recorder
  - music1freq.png, music2freq.png: Fourier transform of **Mary had a little lamp** played by piano and recorder
  - music1overtone.png, music2overtone.png: Overtones distribution of **Mary had a little lamp** played by piano and recorder
  - music1spec.png, music2spec.png: Spectrograms of **Mary had a little lamp** played by piano and recorder by the Gábor transform (overtones filtered)
  - music1score.pdf, music2score.pdf: Music scores generated of **Mary had a little lamp** played by piano and recorder
* Others
  - music1score.ly, music2score.ly: LilyPond files for generating interpretable music scores
