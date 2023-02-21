import { faker } from "@faker-js/faker";
import prisma from "./client.js";
import { categoryList, usersList, entries, distributorList } from "./data.js";

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
  const userMap = new Map();
  const createUsers = [];
  usersList.forEach((user) => {
    createUsers.push({ name: user, email: user + "@gmail.com" });
  });
  await prisma.user.createMany({ data: createUsers });
  const users = await prisma.user.findMany();
  users.forEach((user) => userMap.set(user.name, user));
  const createCats = [];
  const categoryMap = new Map();
  categoryList.forEach((category) => {
    createCats.push({ name: category, description: category });
  });
  await prisma.Category.createMany({ data: createCats });
  const categories = await prisma.Category.findMany();
  categories.forEach((category) => categoryMap.set(category.name, category));
  const createDistributors = [];
  const distributorMap = new Map();
  distributorList.forEach((distributor) =>
    createDistributors.push({ name: distributor })
  );
  await prisma.distributor.createMany({ data: createDistributors });
  const distributors = await prisma.distributor.findMany();
  distributors.forEach((dis) => distributorMap.set(dis.name, dis));
  const createEntryList = [];
  entries.forEach((entry) =>
    createEntryList.push({
      entryUserId: userMap.get(entry.name).id,
      inputDate: new Date(entry.date),
      weight: entry.weight,
      categoryId: categoryMap.get(entry.category).id,
      companyId: distributorMap.get(entry.distributor).id,
    })
  );
  const foodData = await prisma.foodEntry.createMany({ data: createEntryList });
};

try {
  generateFakeData();
} catch (err) {
  console.log(err);
  process.exit(1);
} finally {
  prisma.$disconnect();
}
