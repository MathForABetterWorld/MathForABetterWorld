import express from "express";
import * as express_validator from "express-validator";
import * as validator from "../util/employeeMiddleware.js";
import * as controller from "../controller/employeeController.js";
import { checkToken } from "../util/middleware.js";
const body = express_validator.body;
const param = express_validator.param;

const router = express.Router();
// Here the routes will be listed with correspodning middleware
router.use(checkToken);

//need route for signin
//need route for signout
//need route for promote user
//need route for edit password/username

export default router;
