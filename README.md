# Hand_Tracking
Unlocking the system with hand-tracking

This code is used to unlock the security alert system. 

Introduce of the Security Alert System:
The security alert system is designed to make an alarm (send an SMS) when earthquake, fire, flood, chemical gas leak and sudden change in temperature and humidity. 
It designed with Arduino and Python.

=} Used: Serial Coomunication (PySerial Libary) and MediaPipe

It must be opened with a password set for system operation. With the decision taken, a 5-digit password with hand recognition will be obtained from the user through the cameras included in the system completely without a keyboard.

Hand Landmark Model

![hands](https://user-images.githubusercontent.com/79938189/154844648-6f50dfd0-4430-4832-9d06-40f333aec92a.png)

![hand_crops](https://user-images.githubusercontent.com/79938189/154844706-fce6b934-1d17-4cf6-b010-fb8f1957125b.png)

The part of running this project with a password was done on Python. Used I2C 4x20 - 2x16 LCD Display and Arduino UNO for testing purposes.

## TESTING

![1](https://user-images.githubusercontent.com/79938189/154845688-ce78f132-0e17-4fc4-bb5e-917ad0832b77.jpeg)
![2](https://user-images.githubusercontent.com/79938189/154845690-f9458fe0-8c5d-491d-a359-ef095edb220a.jpeg)
![3](https://user-images.githubusercontent.com/79938189/154845692-77539950-0740-4f23-8ca3-6ecde08c9872.jpeg)
![4](https://user-images.githubusercontent.com/79938189/154845693-920e5c38-fac7-4fea-b28b-1e19850b8b8b.jpeg)


