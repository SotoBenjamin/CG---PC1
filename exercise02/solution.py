
import numpy as np
import cv2
def chessboard_with_custom_colors(WIDTH,HEIGHT,NUM_OF_CELLS_HORIZONTAL,
                                        NUM_OF_CELLS_VERTICAL,COLORS):
    ans = np.zeros((HEIGHT,WIDTH,3),dtype=np.uint8)
    size_V = HEIGHT//NUM_OF_CELLS_VERTICAL
    size_H = WIDTH//NUM_OF_CELLS_HORIZONTAL
    for i in range(NUM_OF_CELLS_VERTICAL):  
        for j in range(NUM_OF_CELLS_HORIZONTAL):
            ans[ i*(size_V):(i+1)*size_V , j*size_H:(j+1)*size_H ] = COLORS[(i+j)%len(COLORS)]
    return ans

colors = [
np.array([0, 0, 0]),
np.array([255, 255, 255]),
np.array([0, 0, 255]),
np.array([0, 255, 0]),
np.array([255, 0, 0]),
np.array([0, 255, 255]),
]

ans = chessboard_with_custom_colors(250,100,13,7,colors)
cv2.imwrite('ans.png',ans)