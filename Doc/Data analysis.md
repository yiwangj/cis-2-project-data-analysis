# Data analysis
To see if color guidance really helps the surgeon in the drilling process, the following comparison was made. We present some results based on common anatomy. Because of the small number of participants and the lack of a concerted effort to target different populations, the study was mainly limited to only demonstrating the utility of the system and recorded data. 
## How to use
### playback video
In order to allow users to visualize the full process of participant drilling and the process of them drilling out the different colored voxels (red for the bad area, yellow for the sensitive area, and green for the part they want to drill out), We made a video of one of the participants drilling a case (available in the wiki), so that users can better understand the whole process of drilling.

### drilling time analysis
using drilling time.py
We calculated the average time to drill in 10 laminectomies for each of the 11 participants, which contained five with color and five with just text. We plotted the boxplot (figure1). In the box plot we can see that there is no significant change in the average time for both, the time with color guidance is rather longer, but we can also find that the distribution of time with color guidance is dense, but the distribution of time without color guidance is highly variance. Although based on the p value of the t-test we believe that the color guidance did not have a significant effect on the drilling time, we can reasonably speculate based on the data that the color guidance did help the physicians to improve the stability and avoid the occurrence of excessively long drilling times.
![Image text](https://github.com/yiwangj/cis-2-project-data-analysis/blob/main/IMG/voxel_remove_time.png)

### drilling force analysis

We studied the effect of color guidance on the force of each stroke, we calculated an average force for each stroke of the participant, and the average force for all strokes in each laminectomies. We can see that the average force with color guidance is lower than without color guidance, and the maximum force with color guidance has a very significant decrease, but since the force used by the participant itself is a very small value during the drilling process, it is difficult to have a very significant difference.


