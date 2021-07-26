# gym-multilayerthinfilm
The proposed OpenAI gym environment utilizes a parallelized transfer-matrix method (TMM) to implement the optimization of for multi-layer thin films as parameterized Markov decision processes. An very intuitve example is provided in example.py.
Whereas the contained physical methods are well-studied and known since decades, the contribution of this code lies the transfer to an OpenAI gym environment. The intention is to enable AI researchers without optical expertise to solve the corresponding parameterized Markov decision processes. Due to their structure, the solution of such problems is still an active field of research in the AI community.<br/>
The publication [Parameterized Reinforcement learning for Optical System Optimization](https://iopscience.iop.org/article/10.1088/1361-6463/abfddb) used this environment.

The environment can include<br/> 
•	cladding of the multi-layer thin film (e.g. substrate and ambient materials),<br/>
•	dispersive and dissipative materials,<br/>
•	spectral and angular optical behavior of multi-layer thin films,<br/>
•	… and many more.<br/>

The environment class allows to <br/>
•	conduct so-called parameterized actions (See publication) that define a multi-layer thin film,<br/>
•	evaluate the generated thin film given a desired optical response, and<br/>
•	render the results. <br/>

In general, the comprehensive optimization of multi-layer thin films in regards of optical reponse encompasses <br/>
•	the number of layers (integer),<br/>
•	the thickness of each layer (float),<br/>
•	the material of each layer (categrial, integer).<br/>
Thus, the optimization features continuous as well as categorial parameters. In the following picture, a stack consisting of 4 layers of particular thicknesses and materials is rendered on the right. The corresponding optical response (here: reflectivity over angle and wavelength) is illustrated on the left. The reward for this state is computed based on a target reflectivity that is specified by the developer.<br/>
![image](https://user-images.githubusercontent.com/83709614/126984626-11c79bc1-720e-41a9-97b2-04e6b602f2cc.png)
