class FileStorage:
    """Serializes instances to a JSON file & deserializes back"""
    def close(self):
        """Call reload() method for deserializing the JSON file to objects"""
        self.reload()
