- [x] Learning rate of 0.01 doesn't seem harmful but rather helpful with combination of clipping with max_Norm 5. Need to explore more here if it can help improving the model.
checked - change is not making much difference either, though 0.01 feels little quick so will settle on 0.001 at least

- [x] also need to try out temperature less than 1 for lower loss; though it didn't work previously but need proper confirmed checking
checked - doesn't seem to make much difference, so keeping the parameter but with value 0.8-1

- [ ] Since the loss is not dropping after 2.2, need more in depth data processing. May have to remove some outliner names but it feels a lot of work for little improvement. So it shall be done after version 2.0

- [ ] For some reason, the torch built-in optimziers are not working. Investigate this further

- [ ] It would be awesome if the generated names can be filtered out by comparing them with lore names before sending them to user. However, this seems little slow but also seems pretty good idea to avoid non-sensical names.

- [ ] a main function integrating both recommender and generator to return the required names

- [ ] import time reduction

- [ ] some better variable names and code restructuring

- [x] a realease as pip package

- [x] a web frontend

- [ ] Since strealit is slow, the flask app would be better to have 

- [ ] a shell script to generate names

- Old model plan -  So far the best working setup has been lr of 0.01 with max_norm=5 and no set temperature value (default=1).

### Current v2 model is with lr of 0.005, max_Norm=5 and temp 0.9 trained on 400k (random and non-unique)names
