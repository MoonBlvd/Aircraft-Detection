import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

class mask():
    mask_id = 1 # 0-left, 1-center, 2-right
    masks = [[1096,1280,290,610],[460,840,200,720],[0,675,900,1800]]
    cmin = masks[mask_id][0]
    cmax = masks[mask_id][1]
    rmin = masks[mask_id][2]
    rmax = masks[mask_id][3]

def findHorizon(img, mask):
    #load user parameters
    user_params = np.loadtxt('user_params.txt')
    print 'get into the function'
    #print user_params

    #Options 1 - along least squares line, 2 - clean sky cut
    seg_type = 2
    
    # Thresholding
    blue_tol = user_params[5]     # rgb blue threshold
    gray_tol = user_params[6]     # rgb gray threshold
    ground_tol = user_params[7]	  # rgb "dark" threshold
    

    blue_check = img[:,:,2] >= blue_tol
    gray_check = (img[:,:,0] >= gray_tol) & (img[:,:,1] >= gray_tol) & (img[:,:,2] >= gray_tol)
    
    sky_pixels = blue_check | gray_check
    ground_pixels = (img[:,:,0] < ground_tol) & (img[:,:,1] < ground_tol) & (img[:,:,2] < ground_tol)
            
    ## Identify image border
    
    # Image size
    imgSize = img.shape
    rows = imgSize[0]
    cols = imgSize[1]

    # Border color: red = (255,43,43)
    border_r = 255
    border_g = 43
    border_b = 43
    
    border_grid = np.zeros((rows,cols))
    border_idx = 1
    border_vals = [0,0]
    # Iterate through all pixels and identify border
    result = img
    
    for x in range (1,(cols-1)):
        for y in range (1, (rows-1)):
            # Set conditions
            cond_ground = ground_pixels[y,x]
            cond1 = sky_pixels[y-1,x]      # pixel up
            cond2 = sky_pixels[y+1,x]      # pixel down
            cond3 = sky_pixels[y,x-1]      # pixel left
            cond4 = sky_pixels[y,x+1]      # pixel right
            
            # Check conditions
            # if one pixel is ground pixel and at least one of its surrounding pixels is sky pixel
            if cond_ground and (cond1 or cond2 or cond3 or cond4):
                # Save border
                border_grid[y,x] = 1
                #border_vals[border_idx,0] = y      # row
                #border_vals[border_idx,1] = x      # column

                border_vals = np.vstack((border_vals,[y,x]))
                border_idx = border_idx + 1
                result[y,x,0] = border_r
                result[y,x,1] = border_g
                result[y,x,2] = border_b

    border_vals = np.delete(border_vals,0,axis = 0)
    print result
    plt.imshow(img)
    plt.imshow(result)
    cv2.waitkey()


    # ## Remove outliers
    # # rows = 1 = y, cols = 2 = x
    
    # dev_allow = user_params[9]     # pixels deviation
    # px_cush = user_params[10]      # px cushion
    
    # # Get info on data set
    # x_max   = max(border_vals[:,1]) 
    # x_min   = min(border_vals[:,1])
    # x_med   = np.median(border_vals[:,1])
    
    # y_max   = max(border_vals[:,0])
    # y_min   = min(border_vals[:,0])
    # y_med   = np.median(border_vals[:,0])

    # # Determine which axis the horizon is along
    # x_num = 0; y_num = 0
    # for i in range (0, border_idx-1):
    #     if abs(border_vals[i,0] - y_med) > dev_allow:
    #         y_num = y_num + 1
        
    #     if abs(border_vals[i,1] - x_med) > dev_allow:
    #         x_num = x_num + 1
    
    # if x_num > y_num:
    #     h_flag = 1
    # else:
    #     h_flag = 0
    
    # clean_border = border_vals[1,:]
    # # Horizontal horizon
    # if h_flag:
    #     # tolerance = avg variance + pixel cushion
    #     tol = mean(abs(border_vals[:,0] - y_med)) + px_cush    
    #     for i in range (1,length(border_vals[:,0])):
    #         # Check mask
    #         if mask.rmin > 0:
    #             rtemp = border_vals[i,0]
    #             ctemp = border_vals[i,1]
    #             #------------------------------------------------------------------------------------------------------------------
    #             mask_check = (rtemp < mask.rmax) and (rtemp > mask.rmin) and (ctemp < mask.cmax) and (ctemp > mask.cmin)
    #         else:
    #             mask_check = 0
    #         end
    #         mask_check = ~mask_check;   # now true = not in mask
            
    #         # Vet values
    #         if (abs(border_vals[i,0]- y_med) <= tol) and mask_check:
    #             # Mark image
    #             result[border_vals[i,0],border_vals[i,1],0] = border_r;
    #             result[border_vals[i,0],border_vals[i,1],1] = border_g;
    #             result[border_vals[i,0],border_vals[i,1],2] = border_b;
    #             # Add new index
    #             clean_idx = [border_vals[i,0], border_vals[i,1]]
    #             clean_border = np.vstack((clean_border, clean_idx))
    # # Vertial horizon
    # else:
    #     # tolerance = avg variance + pixel cushion
    #     tol = mean(abs(border_vals(:,2) - x_med)) + px_cush
    #     for i in range (1, len(border_vals[:,1])):
    #         # Check mask
    #         if mask.rmin > 0:
    #             rtemp = border_vals[i,0]
    #             ctemp = border_vals[i,1]
    #             mask_check = rtemp < mask.rmax && rtemp > mask.rmin...
    #                 && ctemp < mask.cmax && ctemp > mask.cmin;
    #         else:
    #             mask_check = 0
    #         mask_check = ~mask_check;   # now true = not in mask
            
    #         # Vet values
    #         if (abs(border_vals[i,1] - x_med) <= tol) and mask_check:
    #             # Mark image
    #             result[border_vals[i,0],border_vals[i,1],0] = border_r
    #             result[border_vals[i,0],border_vals[i,1],1] = border_g
    #             result[border_vals[i,0],border_vals[i,1],2] = border_b
    #             # Add new index
    #             clean_idx = [border_vals[i,0], border_vals[i,1]
    #             clean_border = [clean_border; clean_idx]

    # # Delete first index
    # clean_border = clean_border[1:len(clean_border[:,1]),:]
    
    # # Clean Sky Cut (skip rest of code)
    # # rows = 1 = y, cols = 2 = x

    # if seg_type == 2:
    #     top_count = 0
    #     bot_count = 0
        
    #     # Horizontal horizon
    #     if h_flag:
    #         line = min(clean_border[:,0])
    #         img_top = img[1:line,:,:]
    #         img_bot = img[line:rows,:,:]
            
    #         for i in range (0, len(border_vals[:,0])):
    #             if (border_vals(i,1) < line):
    #                 top_count = top_count + 1
    #             else:
    #                 bot_count = bot_count + 1

    #     # Vertical horizon
    #     else:
    #         line = min(clean_border[:,1])
    #         img_top = img[:,1:line,:]
    #         img_bot = img[:,line:cols,:]
            
    #         for i in range (0,len(border_vals[:,1])):
    #             if border_vals[i,1] < line:
    #                 top_count = top_count + 1
    #             else
    #                 bot_count = bot_count + 1

    #     # Assign return variables
    #     if bot_count > top_count:
    #         img_sky = img_top
    #         img_ground = img_bot
    #     else:
    #         img_sky = img_bot
    #         img_ground = img_top
        
    #     # Save horizon info
    #     horizon = [line, h_flag]    # line pixel, horizontal/vertical
        
    #     # Show images (testing only)
    #      # cv2.imshow(img_top);
    #      # cv2.imshow(img_bot);
        
    #     # Skip rest of function 
    #     return img_ground, img_sky

if __name__=="__main__":
    img = cv2.imread('cessna.jpg')
    # findHorizon(img)
  
    findHorizon(img,mask)
    # img_ground, img_sky = findHorizon(img,mask)
    # cv2.imshow(img_ground)
    # cv2.imshow(img_sky)
