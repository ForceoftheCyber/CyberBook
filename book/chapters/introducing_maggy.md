# Introducing Maggy

This notebook introduces modeling and control concepts relevant when working with Maggy, the magnetic levitation system.

```{figure} https://github.com/Hansolini/Take-home-Maglev-lab/blob/main/media/images_and_illustrations/maggy_30_levitating.jpg?raw=true
---
name: intro_maggy
align: center
width: 70%
---
Maggy, the magnetic levitation system
```

:::{dropdown} Expand to see videos of Maggy
<div style="display: flex; flex-direction: column; justify-content: center; align-items: center; height: auto; gap: 0.5em; margin-bottom: 1em">
    <iframe 
        width="560"   
        height="300"
        src="https://www.youtube.com/embed/XnbO15yq0vE"
        style="margin: auto"
        frameborder="0"
        allowfullscreen>
    </iframe>
    <iframe 
        width="560"   
        height="300"
        src="https://www.youtube.com/embed/F0SiuVEP2tM"
        style="margin: auto"
        frameborder="0"
        allowfullscreen>
    </iframe>
    <video width="560" height="300" controls>
        <source src="https://github.com/Hansolini/Take-home-Maglev-lab/blob/main/media/videos/maggy_V20_levitation.mp4?raw=true" type="video/mp4">
    </video>
</div>
:::
Maggy is a compact and portable magnetic levitation platform, designed similarly to many other commercial magnetic levitation platforms (https://www.crealev.com/, https://flytestore.com/).

The purpose of Maggy is to make the magnet seen at the top levitate, using an array of permanent magnets (in the image: gray neodymium magnets), electromagnets (in the image: copper coils), and some sensors (not visible).
Ernshaws theorem asserts that stable levitation of any mangetic system containing only passive magnets is impossible! Thus, levitation, such as seen here, can _only_ be achieved with feedback control.

The most important componets of Maggy are:

- **Permanent Magnets**: Four sets of axially magnetized N38 type Neodymium permanent magnets provide the main lift for the levitating magnet.
- **Solenoids:** Four copper air-core solenoids provide corrective magnetic fields for stable levitation.
- **Levitating Magnet:** A large N38 type Neodymium magnet that is being levitated.
- **Hall-effect sensors:** Several digital ratiometric Hall-effect sensors mounted directly on a PCB.
- **Microcontroller:** A Teensy 4.1 microcontroller for reading sensor measurements, and managing power and control signals to the solenoids.

The levitating magnet is free to move and rotate in any direction. The movement is picked-up as changes in the magnetic field measured by the Hall-effect sensors, and this signal can be used as feedback to the solenoids/electromagnets in order to counteract unwanted movement and ensure stable levitation.

## Structure of the book

The goal of this notebook is to make the reader comfortable with the theoretical concepts needed to achieve levitation.
To do so, a simpler "2D" model is used (as will be seen later), but the ideas developed here readily extends to the full "3D" system.

The notebook is designed to guide the reader through the various concepts through text explanations, interactive elements and quizes. We encouraged the reader to take time to answer the questions and proceed only when they are fully understood.
