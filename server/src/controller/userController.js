// Here the functions relating to account db operations will occur
import validate from "../util/checkValidation.js";
import prisma from "../../prisma/client.js";
import { StatusCodes } from "http-status-codes";

export const create = async (req, res) => {
  if (validate(req, res)) {
    return res;
  }
  const { name, email } = req.body;
  const user = await prisma.user.create({ data: { name, email } });
  return res.status(StatusCodes.ACCEPTED).json({ user });
};

export const get = async (req, res) => {
  if (validate(req, res)) {
    return res;
  }
  const users = await prisma.user.findMany({});
  return res.status(StatusCodes.ACCEPTED).json({ users });
};

export const getUserWhoWorkedTheMostHours = async (req, res) => {
  if (validate(req, res)) {
    return res;
  }
  const users = await prisma.user.findMany({
    where: {
      shiftsWorked: {
        isEmpty: false, // we only want users who have worked at least one shift 
      }
    }
  });

  const hashmap = new Map(); // my decision to use Map() instead of POJO {} was arbitrary
  let maxHoursSeen = 0;
  for (const User of users) {
    let totalHours = 0;
    for (const shift of User.shiftsWorked) {
      totalHours += (shift.end - shift.start);
    }
    hashmap.set(totalHours, User);
    maxHoursSeen = Math.max(maxHoursSeen, totalHours);
  }
  let userWhoWorkedTheMostHours = hashmap.get(maxHoursSeen); 

  return res.status(StatusCodes.ACCEPTED).json({ userWhoWorkedTheMostHours });
};

export const update = async (req, res) => {
  if (validate(req, res)) {
    return res;
  }
  const { email, id } = req.body;
  const user = await prisma.user.update({ where: { id }, data: { email } });
  return res.status(StatusCodes.ACCEPTED).json({ user });
};
