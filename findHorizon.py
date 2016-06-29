import cv2
import numpy as np
# def findHorizon(img):
#     # load user parameters
#     f = open('user_params.txt','r')
#     user_params = f.readline()
#     #print user_params

#     #Options 1 - along least squares line, 2 - clean sky cut
#     seg_type = 2
    
#     # Thresholding
#     blue_tol = user_params[6]     # rgb blue threshold
#     gray_tol = user_params[7]     # rgb gray threshold
#     ground_tol = user_params[8]	  # rgb "dark" threshold
    

#     blue_check = img[:,:,2] >= blue_tol
#     gray_check = (img[:,:,0] >= gray_tol) & (img[:,:,1] >= gray_tol) & (img[:,:,2] >= gray_tol)
    
#     sky_pixels = blue_check | gray_check
#     ground_pixels = (img[:,:,1] < ground_tol) & (img[:,:,2] < ground_tol) & (img[:,:,3] < ground_tol)
            
#     ## Identify image border
    
#     # Image size
#     rows, cols = image.shape 
    
#     # Border color: red = (255,43,43)
#     border_r = 255
#     border_g = 43
#     border_b = 43
    
#     border_grid = np.zeros((rows,cols))
#     border_idx = 1
#     border_vals = [];
#     # Iterate through all pixels and identify border
#     result = img
    
#     for x in range (1,(cols-1)):
#         for y in range (1, (rows-1)):
#             # Set conditions
#             cond_ground = ground_pixels[y,x]
#             cond1 = sky_pixels[y-1,x]      # pixel up
#             cond2 = sky_pixels[y+1,x]      # pixel down
#             cond3 = sky_pixels[y,x-1]      # pixel left
#             cond4 = sky_pixels[y,x+1]      # pixel right
            
#             # Check conditions
#             # if one pixel is ground pixel and at least one of its surrounding pixels is sky pixel
#             if cond_ground and (cond1 or cond2 or cond3 or cond4):
#                 # Save border
#                 border_grid[y,x] = 1
#                 #border_vals[border_idx,0] = y      # row
#                 #border_vals[border_idx,1] = x      # column
#                 if not border_vals:
#                     border_vals = [y,x]
#                 else:
#                 	border_vals = np.vstack((border_vals,[y,x]))
#                 border_idx = border_idx + 1
#                 result[y,x,0] = border_r
#                 result[y,x,1] = border_g
#                 result[y,x,2] = border_b
    
#     cv2.imshow(result)
            
#     ## Remove outliers
#     # rows = 1 = y, cols = 2 = x
    
#     dev_allow = user_params[9]     # pixels deviation
#     px_cush = user_params[10]      # px cushion
    
#     # Get info on data set
#     x_max   = max(border_vals[:,1]) 
#     x_min   = min(border_vals[:,1])
#     x_med   = np.median(border_vals[:,1])
    
#     y_max   = max(border_vals[:,0])
#     y_min   = min(border_vals[:,0])
#     y_med   = np.median(border_vals[:,0])

#     # Determine which axis the horizon is along
#     x_num = 0; y_num = 0
#     for i in range (0, border_idx-1):
#         if abs(border_vals[i,0] - y_med) > dev_allow:
#             y_num = y_num + 1
        
#         if abs(border_vals[i,1] - x_med) > dev_allow:
#             x_num = x_num + 1
    
#     if x_num > y_num:
#         h_flag = 1
#     else:
#         h_flag = 0
    
#     clean_border = border_vals[1,:]
#     # Horizontal horizon
#     if h_flag:
#         # tolerance = avg variance + pixel cushion
#         tol = mean(abs(border_vals[:,0] - y_med)) + px_cush    
#         for i in range (1,length(border_vals[:,0])):
#             # Check mask
#             if mask.rmin > 0:
#                 rtemp = border_vals[i,0]
#                 ctemp = border_vals[i,1]
#                 #------------------------------------------------------------------------------------------------------------------
#                 mask_check = (rtemp < mask.rmax) and (rtemp > mask.rmin) and (ctemp < mask.cmax) and (ctemp > mask.cmin)
#             else:
#                 mask_check = 0
#             end
#             mask_check = ~mask_check;   # now true = not in mask
            
#             # Vet values
#             if (abs(border_vals[i,0]- y_med) <= tol) and mask_check:
#                 # Mark image
#                 result[border_vals[i,0],border_vals[i,1],0] = border_r;
#                 result[border_vals[i,0],border_vals[i,1],1] = border_g;
#                 result[border_vals[i,0],border_vals[i,1],2] = border_b;
#                 # Add new index
#                 clean_idx = [border_vals[i,0], border_vals[i,1]]
#                 clean_border = [clean_border; clean_idx]
#     # Vertial horizon
#     else:
#         # tolerance = avg variance + pixel cushion
#         tol = mean(abs(border_vals(:,2) - x_med)) + px_cush
#         for i in range (1, len(border_vals[:,1])):
#             # Check mask
#             if mask.rmin > 0:
#                 rtemp = border_vals[i,0]
#                 ctemp = border_vals[i,1]
#                 mask_check = rtemp < mask.rmax && rtemp > mask.rmin...
#                     && ctemp < mask.cmax && ctemp > mask.cmin;
#             else:
#                 mask_check = 0
#             mask_check = ~mask_check;   # now true = not in mask
            
#             # Vet values
#             if (abs(border_vals[i,1] - x_med) <= tol) and mask_check:
#                 # Mark image
#                 result[border_vals[i,0],border_vals[i,1],0] = border_r
#                 result[border_vals[i,0],border_vals[i,1],1] = border_g
#                 result[border_vals[i,0],border_vals[i,1],2] = border_b
#                 # Add new index
#                 clean_idx = [border_vals[i,0], border_vals[i,1]
#                 clean_border = [clean_border; clean_idx]

#     # Delete first index
#     clean_border = clean_border[1:len(clean_border[:,1]),:]
    
#     # Clean Sky Cut (skip rest of code)
#     # rows = 1 = y, cols = 2 = x

#     if seg_type == 2
#         top_count = 0;
#         bot_count = 0;
        
#         # Horizontal horizon
#         if h_flag
#             line = min(clean_border(:,1));
#             img_top = img(1:line,:,:);
#             img_bot = img(line:end,:,:);
            
#             for i = 1:length(border_vals(:,1))
#                 if (border_vals(i,1) < line)
#                     top_count = top_count + 1;
#                 else
#                     bot_count = bot_count + 1;
#                 end
#             end
#         # Vertical horizon
#         else
#             line = min(clean_border(:,2));
#             img_top = img(:,1:line,:);
#             img_bot = img(:,line:end,:);
            
#             for i = 1:length(border_vals(:,2))
#                 if (border_vals(i,2) < line)
#                     top_count = top_count + 1;
#                 else
#                     bot_count = bot_count + 1;
#                 end
#             end
#         end

#         # Assign return variables
#         if bot_count > top_count
#             img_sky = img_top;
#             img_ground = img_bot;
#         else
#             img_sky = img_bot;
#             img_ground = img_top;
#         end
        
#         # Save horizon info
#         horizon = [line, h_flag];    # line pixel, horizontal/vertical
        
#         # Show images (testing only)
#          # figure(1); imshow(img_top);
#          # title('Top'); set(gca,'FontSize',14);
#          # figure(2); imshow(img_bot);
#          # title('Bottom'); set(gca,'FontSize',14);
        
#         # Skip rest of function 
#         return

if __name__=="__main__":
    img = cv2.imread('cessna.jpg')
    # findHorizon(img)
    a = [1,2]
    a = np.vstack((a,[[1,2]]))
    a = np.vstack((a,[[3,4]]))
    print a

    a = []
    if not a:
        a = [1,2]
        print a