smallest_pyramid = 1 # global

blocks = int(input("Enter the amount of blocks you have: "))

# If the given amount of blocks is smaller than the smallest buildable pyramid
if blocks <= smallest_pyramid:
    print(f"It is not possible to build a pyramid with {blocks} blocks!")    
else:
    height, needed_blocks  = 0, 1
    
    # Check if the pyramid can be built by comparing the remaining blocks
    # to the block amount needed to complete the next layer
    can_be_built = blocks >= needed_blocks

    while can_be_built:
        # Add a layer to the pyramid
        height += 1
        # Remove previously used blocks from the block amount
        blocks -= needed_blocks
        # Calculate the next layer's needed block amount
        needed_blocks += 1
        # Check if there are enough blocks to build the next layer
        can_be_built = blocks >= needed_blocks

print(f"The height of the pyramid: {height}")
