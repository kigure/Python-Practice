from mcpi import minecraft, block


def main():
    mc = minecraft.Minecraft.create()
    mc.player.setPos(0, 1, 0)
    mc.setBlocks(
        -3, 0, -3,   # blockを置きはじめる位置
        50, 50, 50,  # blockの置き終わり位置
        block.AIR    # どんなblockを置くか
    )
    mc.setBlocks(
        -3, 0, -3,
        50, 0, 50,
        block.SNOW_BLOCK
    )


if __name__ == "__main__":
    main()
