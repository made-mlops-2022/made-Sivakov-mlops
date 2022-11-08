import pickle


class PersistenceModelManager:

    @staticmethod
    def serialize_model_to_file(model, filename: str):
        with open(filename, 'wb') as f:
            pickle.dump(model, f)

    @staticmethod
    def deserialize_model_from_file(filename: str):
        with open(filename, 'rb') as f:
            return pickle.load(f)
