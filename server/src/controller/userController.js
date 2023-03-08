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
    include: {
      shiftsWorked: true,
    },
  });

  const hashmap = new Map(); // my decision to use Map() instead of POJO {} was arbitrary
  let maxHoursSeen = 0;
  for (const User of users) {
    let totalHours = 0;
    for (const shift of User.shiftsWorked) {
      totalHours += shift.end - shift.start;
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

/**
 * Gets total volunteer hours worked for a specific "user"
 * @param {object} req - request for the course
 * @param {object} res - response for the request
 */
export const getTotalUserHours = async (req, res, userId) => {
  if (validate(req, res)) {
    return res;
  }
  const id = parseInt(req.params.userId); // request as input a user id
  const userHours = await prisma.shift.aggregate({
    where: {
      userId: id, // filter the shift table based on the input user id
      not: [
        {
          end: null,
        },
      ],
    },
    _sum: {
      duration,
      // : {
      //   _divide: [
      //     { _subtract: ["end", "start"] }, // subtract outimes difference in milliseconds
      //     3600000 // convert milliseconds to hours
      //   ]
      // }
    },
  });
  return res.status(StatusCodes.OK).json({ userHours });
};
