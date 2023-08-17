scene.set_background_image(assets.image("""
    myImage0
"""))
mySprite = sprites.create(assets.image("""
    myImage
"""), SpriteKind.player)
mySprite.set_bounce_on_wall(True)