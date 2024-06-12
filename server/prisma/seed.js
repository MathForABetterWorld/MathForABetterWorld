import { faker } from "@faker-js/faker";
import prisma from "./client.js";
import { Role } from "@prisma/client";
import { hashPassword } from "../src/util/password.js";
import {
  categoryList,
  usersList,
  entries,
  distributorList,
  exportsList,
  shiftList,
  donatedToList,
  rackList,
} from "./data.js";

const generateFakeUsers = async (numFakeUsers) => {
  for (let index = 0; index < numFakeUsers; index++) {
    const firstName = faker.name.firstName();
    const lastName = faker.name.lastName();
    const email = faker.internet.email(firstName, lastName, "fakerjs.dev");
    await prisma.user.create({
      data: {
        email: email.toLowerCase(),
        name: `${firstName} ${lastName}`,
      },
    });
  }
};

const generateFakeData = async () => {
  // await prisma.user.deleteMany();
  // await generateFakeUsers(3);
  const locationMap = new Map();
  const createLocations = [];
  const locationSet = new Set();
  donatedToList.forEach((location) => {
    if (!locationSet.has(location)) {
      createLocations.push({
        name: location.name,
        longitude: location.longitude,
        latitude: location.latitude,
      });
      locationSet.add(location);
    }
  });
  await prisma.donationLocation.createMany({ data: createLocations });
  const locations = await prisma.donationLocation.findMany();
  locations.forEach((loc) => locationMap.set(loc.name, loc));
  const userMap = new Map();
  const userSet = new Set();
  const createUsers = [];
  usersList.forEach((user) => {
    if (!userSet.has(user)) {
      createUsers.push({
        name: user,
        email: user.replace(/\s+/g, "") + "@gmail.com",
      });
      userSet.add(user);
    }
  });
  await prisma.user.createMany({ data: createUsers });
  const users = await prisma.user.findMany();
  users.forEach((user) => userMap.set(user.name, user));
  const createCats = [];
  const categoryMap = new Map();
  const categorySet = new Set();
  categoryList.forEach((category) => {
    if (!categorySet.has(category)) {
      createCats.push({ name: category, description: category });
      categorySet.add(category);
    }
  });
  await prisma.category.createMany({ data: createCats });
  const categories = await prisma.category.findMany();
  categories.forEach((category) => categoryMap.set(category.name, category));
  const createDistributors = [];
  const distributorMap = new Map();
  distributorList.forEach((distributor) =>
    createDistributors.push({ name: distributor })
  );
  await prisma.distributor.createMany({ data: createDistributors });
  const distributors = await prisma.distributor.findMany();
  distributors.forEach((dis) => distributorMap.set(dis.name, dis));
  const createRacks = [];
  const rackMap = new Map();
  rackList.forEach((rack) => {
    createRacks.push({
      location: rack.location,
      description: rack.description,
      weightLimit: rack.weightLimit,
    });
  });
  await prisma.rack.createMany({ data: createRacks });
  const racks = await prisma.rack.findMany();
  racks.forEach((rack) => rackMap.set(rack.location, rack));
  const createEntryList = [];
  entries.forEach((entry) => {
    if (rackMap.has(entry.rack)) {
      createEntryList.push({
        entryUserId: userMap.get(entry.name).id,
        inputDate: new Date(entry.date),
        weight: entry.weight,
        categoryIds: [categoryMap.get(entry.category).id],
        companyId: distributorMap.get(entry.distributor).id,
        rackId: rackMap.get(entry.rack).id,
      });
    } else {
      createEntryList.push({
        entryUserId: userMap.get(entry.name).id,
        inputDate: new Date(entry.date),
        weight: entry.weight,
        categoryIds: categoryMap.get(entry.category).id,
        companyId: distributorMap.get(entry.distributor).id,
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
        userId: userMap.get(exportItem.name).id,
        exportDate: new Date(exportItem.date),
        weight: exportItem.weight,
        categoryId: categoryMap.get(exportItem.category).id,
        locationId: locationMap.get(exportItem.location).id,
        rackId: rackMap.get(exportItem.rack).id,
        exportType: exportType,
      });
    } else {
      createExportsList.push({
        userId: userMap.get(exportItem.name).id,
        exportDate: new Date(exportItem.date),
        weight: exportItem.weight,
        categoryId: categoryMap.get(exportItem.category).id,
        locationId: locationMap.get(exportItem.location).id,
        exportType: exportType,
      });
    }
  });
  await prisma.exportItem.createMany({
    data: createExportsList,
  });
  const default_admin = await prisma.user.create({
    data: {
      email: "bcfdashboard@gmail.com",
      name: "Default Admin",
    },
  });
  await prisma.employee.createMany({
    data: [
      {
        userId: default_admin.id,
        userName: "default_admin",
        hashedPassword: hashPassword("default_admin"),
        role: Role.Admin,
      },
    ],
  });
  const defaultEmployee = await prisma.employee.findFirst({
    where: {
      userId: default_admin.id,
    },
  });
  await prisma.user.update({
    where: {
      id: default_admin.id,
    },
    data: {
      employeeId: defaultEmployee.id,
    },
  });
  const createShiftList = [];
  shiftList.forEach((entry) => {
    if (userMap.get(entry.name)) {
      createShiftList.push({
        userId: userMap.get(entry.name).id,
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
