# Week 4 Assignment ESRGAN
ESRGAN model uses a relativistic discriminator, an RRDB based generator and also incorporates perceptual loss. The main ideas implemented are based on the original paper of ESRGAN.

## Basic Functioning
- Basically, the functioning of ESRGAN is similar to a typical GAN with some modifications. The working of a GAN is quite simple, the generator produces an output, the discriminator then tries to determine if the output is a realistic high resolution image and then based on the output of the discriminator, the generator values are tuned.
- The perceptual loss and VGG loss are 2 major additions to the basic model of SRGAN. They make the images look more realistic. This is because these losses corelate more strongly to human image perception itself rather than a standard loss function like mean squared loss.
- Major addition to ESRGAN model is the use of RRDBs which are not used in SRGAN.
