class GameService:
    """service provides collision handler"""
    @staticmethod
    def is_batch_in_collisions(list_of_nodes, collisions):
        for nodes in list_of_nodes:
            for el in nodes:
                if el in collisions:
                    return el
        return False

    @staticmethod
    def collision_handler(list_of_nodes, collisions):
        for el in list_of_nodes:
            if el in collisions:
                return el
        return False
