import numpy as np
import cv2
def chessboard_with_custom_colors(WIDTH_IN_PIXELS,HEIGHT_IN_PIXELS,NUM_OF_CELLS_HORIZONTAL,
                                        NUM_OF_CELLS_VERTICAL,COLORS):
    ans = np.zeros((HEIGHT_IN_PIXELS,WIDTH_IN_PIXELS,3),dtype=np.uint8)
    size_V = HEIGHT_IN_PIXELS//NUM_OF_CELLS_VERTICAL
    size_H = WIDTH_IN_PIXELS//NUM_OF_CELLS_HORIZONTAL
    for i in range(NUM_OF_CELLS_VERTICAL):  
        for j in range(NUM_OF_CELLS_HORIZONTAL):
            ans[ i*(size_V):(i+1)*size_V , j*size_H:(j+1)*size_H ] = COLORS[(i+j)%len(COLORS)]
    return ans

