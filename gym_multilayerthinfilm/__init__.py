"""
          Reinforcement learning is an area of machine learning concerned with how intelligent agents ought to take actions in an environment in order to maximize
          the notion of reward. The code to be published implements such an environment for the optimization of multi-layer thin films.
        	In principle, the proposed code allows to execute actions taken by an agent.
          These actions determine which material of which thickness to stack next, thereby consecutively forming a multi-layer thin film.
          Such a multi-layer thin film exhibits optical characteristics. By comparison between the actual and user-defined desired characteristics,
          a notion of numeric reward is computed based on which the agent learns to distinguish between good and bad design choices. Namely, the agent can steer each
          layer’s material and thickness as well as the total number of layers.
          Thus, reinforcement learning can be used to optimize multi-layer thin films in regards of their optical characteristics.  
          Among others, the environment implements the execution of actions via step-method, the rendering of suggested multi-layer thin films and the reward computation.

                Args to create the environment gym_multilayerthinfilm.MultiLayerThinFilm:

                  N:                  np.array of shape [M x S]
                where M is the number of available materials and S is the number of supporting points of the spectrum
                N holds the (dispersive, complex) refractive indicies of the available materials
            maximum_layers:     integer
                maximum_layers defines the maximum number of layers to stack
            target:             dictionary
                with keys 'target', 'direction', 'spectrum'
                target['direction'] holds the angles [deg, °] under consideration and is of shape D
                target['spectrum'] holds the spectrum [m] under consideration and is of shape S
                target['target'] holds the pixel-wise target reflectivity of a MLTF and is of shape [D x S]
            weights:            np.array of same shape [D x S]
                This array allows to steer the pixels relative influence on the optimization/reward
            normalization:      Boolean
                Determines whether to exponentially transform the reward or not (Look publication for details)
            sparse_reward:      Boolean
                Determines whether to simulate and reward each intermediate stack or only the final stack
            substrate:          dictionary or None
                Holds the (dispersive, complex) refractive indicies of the substrate materials in the rows of
                substrate['n'] which is of shape np.array of shape [Sub x S] . Sub is the number of materials that form
                the substrate. substrate['d'] is of shape Sub and holds the corresponding thicknesses of each layer.
                If substrate is None (default) it is set to vacuum of infinite thickness.
            ambient:            dictionary or None
                Holds the (dispersive, complex) refractive indicies of the ambient materials in the rows of
                ambient['n'] which is of shape np.array of shape [Am x S] . Am is the number of materials that form
                the ambient. ambient['d'] is of shape Am and holds the corresponding thicknesses of each layer.
                If ambient is None (default) it is set to vacuum of infinite thickness.
            max_thickness:      float
                Determines the maximum layer thickness in meter.
            min_thickness:      float
                Determines the minimum layer thickness in meter.
            work_path:          str
                Path to working directory e.g. to save images        
        """

from gym_multilayerthinfilm import *
from gym_multilayerthinfilm.utils import *
from gym_multilayerthinfilm.gym_class import *

