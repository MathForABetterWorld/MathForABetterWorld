import express from "express";
import * as express_validator from "express-validator";

const body = express_validator.body;
const param = express_validator.param;

const router = express.Router();
// Here the routes will be listed with correspodning middleware

// Example routes from another app:
/**
 * router.post(
  "/signup",
  body("email", "Email is required").isEmail(),
  body("name", "Name is required").notEmpty(),
  body("phoneNumber").optional().isMobilePhone(),
  validator.isUniqueEmail,
  validator.isUniquePhone,
  controller.create
);

router.post(
  "/login",
  body("email", "Email is required").isEmail(),
  validator.emailExists,
  controller.login
);
 */

// Guide: https://www.prisma.io/docs/concepts/components/prisma-client/crud

export default router;
