import axios from "axios";

const URL = "https://api.barcodelookup.com/v3/products?";
const key = "pwyejmhch3uj5kbk43z1vg2z5dmbhg";

export const barcodeUPCApi = async (UPC) => {
  let urlToCall = URL + "barcode=" + UPC + "&formatted=y&key=" + key;
  axios
    .get(urlToCall)
    .then(function (response) {
      // handle success
      console.log(response);
      return response;
    })
    .catch(function (error) {
      // handle error
      console.log(error);
    })
    .finally(function () {});
};
