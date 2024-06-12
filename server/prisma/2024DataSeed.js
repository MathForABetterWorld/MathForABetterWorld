import { faker } from "@faker-js/faker";
import prisma from "./client.js";
import { Role } from "@prisma/client";
import { hashPassword } from "../src/util/password.js";

import {
  volunteerList,
  importsList,
  exportsList,
  distributorList,
} from "./2024Data.js";

const generateFakeData = async () => {
  // await prisma.user.deleteMany();
  // await generateFakeUsers(3);
  const locationMap = new Map();
  const locations = await prisma.donationLocation.findMany();
  locations.forEach((loc) => locationMap.set(loc.name.toLowerCase(), loc));
  const userMap = new Map();
  const users = await prisma.user.findMany();
  users.forEach((user) => userMap.set(user.name.toLowerCase(), user));
  const categoryMap = new Map();
  const categories = await prisma.category.findMany();
  categories.forEach((category) =>
    categoryMap.set(category.name.toLowerCase(), category)
  );
  const createDistributors = [];
  const distributorMap = new Map();
  distributorList.forEach((distributor) =>
    createDistributors.push({ name: distributor })
  );
  await prisma.distributor.createMany({ data: createDistributors });
  const distributors = await prisma.distributor.findMany();
  distributors.forEach((dis) =>
    distributorMap.set(dis.name.toLowerCase(), dis)
  );
  const rackMap = new Map();
  const racks = await prisma.rack.findMany();
  racks.forEach((rack) => rackMap.set(rack.location.toLowerCase(), rack));
  const createEntryList = [];
  importsList.forEach((entry) => {
    if (rackMap.has(entry.rack)) {
      createEntryList.push({
        entryUserId: userMap.get(entry.name.toLowerCase()).id,
        inputDate: new Date(entry.date),
        weight: entry.weight,
        categoryIds: [categoryMap.get(entry.category.toLowerCase()).id],
        companyId: distributorMap.get(entry.distributor.toLowerCase()).id,
        rackId: rackMap.get(entry.rack).id,
      });
    } else {
      console.log(entry);
      createEntryList.push({
        entryUserId: userMap.get(entry.name.toLowerCase()).id,
        inputDate: new Date(entry.date),
        weight: entry.weight,
        categoryIds: categoryMap.get(entry.category.toLowerCase()).id,
        companyId: distributorMap.get(entry.distributor.toLowerCase()).id,
      });
    }
  });
  await prisma.pallet.createMany({ data: createEntryList });
  const createExportsList = [];
  exportsList.forEach((exportItem) => {
    let exportType = "Regular";

    if (exportItem.weight < 0) {
      exportType = "Return";
    }
    if (rackMap.has(exportItem.rack)) {
      createExportsList.push({
        userId: userMap.get(exportItem.name.toLowerCase()).id,
        exportDate: new Date(exportItem.date.toLowerCase()),
        weight: exportItem.weight,
        categoryId: categoryMap.get(exportItem.category.toLowerCase()).id,
        locationId: locationMap.get(exportItem.location.toLowerCase()).id,
        rackId: rackMap.get(exportItem.rack.toLowerCase()).id,
        exportType: exportType,
      });
    } else {
      console.log(exportItem);
      createExportsList.push({
        userId: userMap.get(exportItem.name.toLowerCase()).id,
        exportDate: new Date(exportItem.date),
        weight: exportItem.weight,
        categoryId: categoryMap.get(exportItem.category.toLowerCase()).id,
        locationId: locationMap.get(exportItem.location.toLowerCase()).id,
        exportType: exportType,
      });
    }
  });
  await prisma.exportItem.createMany({
    data: createExportsList,
  });
  const createShiftList = [];
  volunteerList.forEach((entry) => {
    if (userMap.get(entry.name)) {
      createShiftList.push({
        userId: userMap.get(entry.name.toLowerCase()).id,
        start: new Date(entry.start),
        end: new Date(entry.end),
        regularFoodTaken: entry.regularTaken,
        damagedFoodTaken: entry.damagedTaken,
      });
    } else {
      console.log(entry.name);
    }
  });
  await prisma.shift.createMany({ data: createShiftList });
};

try {
  generateFakeData();
} catch (err) {
  console.log(err);
  process.exit(1);
} finally {
  prisma.$disconnect();
}
