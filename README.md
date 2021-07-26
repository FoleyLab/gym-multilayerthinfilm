# gym-multilayerthinfilm
The proposed OpenAI gym environment utilizes a parallelized transfer-matrix method (TMM) to implement the optimization of for multi-layer thin films as parameterized Markov decision processes. An very intuitve example is provided in example.py.

The environment can include 
•	cladding of the multi-layer thin film (e.g. substrate and ambient materials)
•	dispersive and dissipative materials
•	spectral and angular optical behavior of multi-layer thin films
•	… and many more

The environment class allows to 
•	conduct so-called parameterized actions (See publication) that define a multi-layer thin film,
•	evaluate the generated thin film given a desired optical response and
•	render the results 
Whereas the contained physical methods are well-studied and known since decades, the contribution of this code lies the transfer to an OpenAI gym environment. The intention is to enable AI researchers without optical expertise to solve the corresponding parameterized Markov decision processes. Due to their structure, the solution of such problems is still an active field of research in the AI community. 

In general, the comprehensive optimization of multi-layer thin films in regards of optical reponse encompasses 
•	the number of layers (integer),
•	the thickness of each layer (float),
•	the material of each layer (categrial, integer).
Thus, the optimization features continuous as well as categorial parameters. In the following picture, a stack consisting of 4 layers of particular thicknesses and materials is rendered on the right. The corresponding optical response (here: reflectivity over angle and wavelength) is illustrated on the left. The reward for this state is computed based on a target reflectivity that is specified by the developer.
![image](https://user-images.githubusercontent.com/83709614/126982644-ae4eed99-df34-4d59-8abe-794a72a51409.png)
