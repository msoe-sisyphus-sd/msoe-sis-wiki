

# Music to Color Algorithmic Approaches


# What gives Music Color?

[https://journals.sagepub.com/doi/pdf/10.1177/2041669518808535](https://journals.sagepub.com/doi/pdf/10.1177/2041669518808535) 



*   Arousal 
*   Valence 


# How can we turn Audio into Features?



*   Great question. There are a few possibilities--
*   [https://github.com/MixedEmotions/up_emotions_audio](https://github.com/MixedEmotions/up_emotions_audio) 
*   [https://github.com/Dohppak/Music_Emotion_Recognition](https://github.com/Dohppak/Music_Emotion_Recognition) 
*   [https://github.com/topel/emoMusic](https://github.com/topel/emoMusic) 
    *   Really interesting paper attached to this, unfortunately the code is pretty terrible and has zero documentation
*   [https://towardsdatascience.com/predicting-the-music-mood-of-a-song-with-deep-learning-c3ac2b45229e](https://towardsdatascience.com/predicting-the-music-mood-of-a-song-with-deep-learning-c3ac2b45229e) 
*   [https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=9229494](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=9229494) 
    *   Highlights the issues associated with trying to use a small number of features to describe the mood audio.
*   [https://www.researchgate.net/publication/324093990_Novel_Audio_Features_for_Music_Emotion_Recognition?enrichId=rgreq-101165b71d18a62f1c3cd0ad596194ab-XXX&enrichSource=Y292ZXJQYWdlOzMyNDA5Mzk5MDtBUzo2NjkyNTU5NTk4NDY5MTdAMTUzNjU3NDQ2MzM1Mg%3D%3D&el=1_x_2&_esc=publicationCoverPdf](https://www.researchgate.net/publication/324093990_Novel_Audio_Features_for_Music_Emotion_Recognition?enrichId=rgreq-101165b71d18a62f1c3cd0ad596194ab-XXX&enrichSource=Y292ZXJQYWdlOzMyNDA5Mzk5MDtBUzo2NjkyNTU5NTk4NDY5MTdAMTUzNjU3NDQ2MzM1Mg%3D%3D&el=1_x_2&_esc=publicationCoverPdf) 
    *   Underscores how difficult it is to obtain a dataset that’s reliable
    *   
*   [https://sites.tufts.edu/eeseniordesignhandbook/2015/music-mood-classification/](https://sites.tufts.edu/eeseniordesignhandbook/2015/music-mood-classification/) 
    *   This is a nice way of doing audio classification, as it gives us more concrete and detectable features with which to classify music, using pitch, intensity, timbre and rhythm. 
*   Classifying Timbre is apparently possible. This article presents some classification equations, but ultimately doesn’t come up with a simplified formula (highly disappointed).
    *   [https://digitalcommons.sacredheart.edu/cgi/viewcontent.cgi?referer=https://www.google.com/&httpsredir=1&article=1015&context=wac_prize](https://digitalcommons.sacredheart.edu/cgi/viewcontent.cgi?referer=https://www.google.com/&httpsredir=1&article=1015&context=wac_prize) 
*   Pitch
    *   [https://aubio.org/manual/latest/index.html](https://aubio.org/manual/latest/index.html)
*   Classified dataset
    *   [http://www2.projects.science.uu.nl/memotion/emotifydata/](http://www2.projects.science.uu.nl/memotion/emotifydata/)
    *   Site if data is used


# How Do We Decide?



*   Decision Matrix:

<table>
  <tr>
   <td>
<strong>Vectors:</strong>
   </td>
   <td><strong>Machine Learning</strong>
   </td>
   <td><strong>Non-Machine Learning</strong>
   </td>
  </tr>
  <tr>
   <td>Open Licensing Available?
   </td>
   <td>Yes
   </td>
   <td>Yes
   </td>
  </tr>
  <tr>
   <td>Effort to Implement (0-5, 0 is easy)
   </td>
   <td>3
   </td>
   <td>2-5
   </td>
  </tr>
  <tr>
   <td># of Dependency Libraries
   </td>
   <td>6
   </td>
   <td>2
   </td>
  </tr>
  <tr>
   <td>CPU / Performance (0-5, each point = 20%)
   </td>
   <td> 2-3 (decently optimized, thanks to Andy's work)
   </td>
   <td>1 (unoptimized)
   </td>
  </tr>
  <tr>
   <td>Ease of Maintenance  (0-5, 0 is easy)
   </td>
   <td> 2 (will occaisionally require an updated model for new `sklearn` versions)
   </td>
   <td>2
   </td>
  </tr>
  <tr>
   <td>Efficacy  (0-5, 0 is ineffective)
   </td>
   <td> 4 (works decently well, per existing tests)
   </td>
   <td>3? (untested+unoptimized)
   </td>
  </tr>
  <tr>
   <td><strong>TOTALS</strong>
   </td>
   <td>
   </td>
   <td>10-15
   </td>
  </tr>
</table>



# Machine Learning: Homegrown vs OFTS:

In my professional opinion, pursuing an OFTS solution will be the easiest for our team. Attempts at creating a home-grown algorithm have stalled largely due to the issues associated with obtaining a suitable dataset. Suitable datasets have dozens of features, and many notable research papers have described the difficulties associated with trying to create an effective model using 5 or fewer features. This creates a complex feature space to work with, doable given a good dataset, but impossible if the dataset provided does not have enough features to work with.

If a large enough dataset could be procured, this option might be more viable. Alternatively, a dataset could potentially be “mined” from a source, but this would require time and effort. Finally, the lack of team knowledge about machine learning might make future development on a model difficult. While this does not excuse the team of exploring a machine learning algorithm grown from home, it does raise the cost of initial time-wise investment.

Given that the existing algorithm used by the team is roughly CPU-efficient and has a set mode, and uses close to 130 features to predict an output, the quality of the model produced is much higher than one currently within reach of our training abilities.

Formal Recommendation: Obtain the dataset from the author in case of a need to train future models, and proceed with existing algorithm IF machine learning is chosen as the algorithm to proceed with.
