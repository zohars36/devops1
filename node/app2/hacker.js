const axios = require("axios");

const getRest = async (city, maxCost) => {
  let pageNo = 1;
  let list = [];
  try {
    while (1) {
      console.log("Page No: " + pageNo);
      const res = await axios.get(
        "https://jsonmock.hackerrank.com/api/food_outlets?city=" +
          city +
          "&page=" +
          pageNo
      );
      //console.log(res.data);
      let rest = res.data.data;
      rest.forEach((item) => {
        console.log(item.estimated_cost);
        if (item.estimated_cost <= maxCost) {
          console.log(item.name);
          list.push(item.name);
        }
      });
      if (pageNo >= res.data.total_pages) {
        break;
      }
      pageNo++;
    }
    return list;
  } catch (e) {
    console.log(e);
  }
};

async function main() {
  try {
    console.log("Zohar1");
    const restList = await getRest("Denver", 50);
    console.log("Zohar2");
    console.log(restList.join(""));
    console.log("Zohar3");
  } catch (e) {
    console.log(e);
  }
}

main();
