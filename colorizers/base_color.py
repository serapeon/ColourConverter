"""Shared L*a*b* channel normalisation helpers for the colorization models.

BaseColor centres and scales the L (lightness) and ab (colour) channels of a
CIE L*a*b* image into the range the pretrained eccv16/siggraph17 networks
were trained on, and reverses that scaling on their predictions.
"""

import torch
from torch import nn

class BaseColor(nn.Module):
	"""Provides L*a*b* channel normalisation shared by the colorization models.

	Subclasses (ECCVGenerator, SIGGRAPHGenerator) feed normalised channels
	into the network and unnormalise its output back to real L*a*b* values.
	"""

	def __init__(self):
		super(BaseColor, self).__init__()

		self.l_cent = 50.
		self.l_norm = 100.
		self.ab_norm = 110.

	def normalize_l(self, in_l):
		"""Centres and scales a raw L channel (range 0-100) to roughly [-1, 1]."""
		return (in_l-self.l_cent)/self.l_norm

	def unnormalize_l(self, in_l):
		"""Reverses `normalize_l`, returning a raw L channel (range 0-100)."""
		return in_l*self.l_norm + self.l_cent

	def normalize_ab(self, in_ab):
		"""Scales raw ab channels to roughly the [-1, 1] range."""
		return in_ab/self.ab_norm

	def unnormalize_ab(self, in_ab):
		"""Reverses `normalize_ab`, returning raw ab channel values."""
		return in_ab*self.ab_norm
