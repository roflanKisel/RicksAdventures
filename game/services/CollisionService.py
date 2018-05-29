class CollisionService:
    """class is needed to add objects to collision manager"""
    @staticmethod
    def wall_init_batch_node(collision_manager, batch, barriers):
        for walls in barriers:
            for wall in walls:
                collision_manager.add(wall)
                batch.add(wall)

    @staticmethod
    def entity_init_batch_node(collision_manager, batch, enemies):
        for enemy in enemies:
            collision_manager.add(enemy)
            batch.add(enemy)
