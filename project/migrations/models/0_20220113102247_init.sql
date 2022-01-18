-- upgrade --
CREATE TABLE IF NOT EXISTS "bank" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "Bank_Name" VARCHAR(50) NOT NULL,
    "Bank_Masked_Name" VARCHAR(50) NOT NULL,
    "Toggle_Display" BOOL NOT NULL
);
CREATE TABLE IF NOT EXISTS "banker" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "Bank" VARCHAR(100) NOT NULL,
    "Market_Segment" VARCHAR(100) NOT NULL,
    "Banker_Name" VARCHAR(100) NOT NULL,
    "Banker_Contact_No" BIGINT NOT NULL,
    "Banker_Email_Address" VARCHAR(100) NOT NULL,
    "Remarks" TEXT NOT NULL,
    "Banker_Start_Date" DATE,
    "Banker_End_Date" DATE,
    "Banker_status" VARCHAR(20) NOT NULL
);
CREATE TABLE IF NOT EXISTS "segment" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "Segment_Name" VARCHAR(100) NOT NULL,
    "Toggle_Segment" BOOL NOT NULL,
    "owner_id" INT NOT NULL REFERENCES "banker" ("id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(20) NOT NULL,
    "content" JSONB NOT NULL
);
