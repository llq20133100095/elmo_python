from allennlp.commands.elmo import ElmoEmbedder
from allennlp.modules.elmo import Elmo, batch_to_ids
import numpy as np

def elmo_use():
	options_file = "./elmo_2x4096_512_2048cnn_2xhighway_options.json"
	weight_file = "./elmo_2x4096_512_2048cnn_2xhighway_weights.hdf5"

	elmo = ElmoEmbedder(options_file, weight_file)

	# use batch_to_ids to convert sentences to character ids
	context_tokens = [['I', 'love', 'you', '.'], ['Sorry', ',', 'I', 'don', "'t", 'love', 'you', '.']] #references
	elmo_embedding, elmo_mask = elmo.batch_to_embeddings(context_tokens)

	print(elmo_embedding)
	elmo_embedding=np.array(elmo_embedding)
	return elmo_embedding


def elmo_use2():
	options_file = "https://s3-us-west-2.amazonaws.com/allennlp/models/elmo/2x4096_512_2048cnn_2xhighway/elmo_2x4096_512_2048cnn_2xhighway_options.json"
	weight_file = "https://s3-us-west-2.amazonaws.com/allennlp/models/elmo/2x4096_512_2048cnn_2xhighway/elmo_2x4096_512_2048cnn_2xhighway_weights.hdf5"

	elmo = Elmo(options_file, weight_file, 3, dropout=0)

	# use batch_to_ids to convert sentences to character ids
	sentences = [['First', 'sentence', '.'], ['Another', '.']]
	character_ids = batch_to_ids(sentences)

	embeddings = elmo(character_ids)

	a=np.array(embeddings)
	return a
