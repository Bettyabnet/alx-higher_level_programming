#!/usr/bin/node
/*
 * Here's an updated version of the 101-call_me_moby.js file
 */
exports.callMeMoby = function (x, theFunction) {
  if (x > 0) {
    theFunction();
    exports.callMeMoby(x - 1, theFunction);
  }
};
