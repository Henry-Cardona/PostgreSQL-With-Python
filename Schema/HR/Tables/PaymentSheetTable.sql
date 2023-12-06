
CREATE TABLE
	HR.PAYMENT_SHEET (
        /*
        *   UNIQUE FILD
        */
        ID_PAYMENT_SHEET UUID DEFAULT uuid_generate_v4 () PRIMARY KEY,
		/*
        *   THESE FIELDS STORE PAYMENT SHEET INFORMATION 
        *   TO BE ABLE TO IDENTIFY IT
        */
		START_DATE_PAYMENT_SHEET DATE,
        END_DATE_PAYMENT_SHEET DATE,
        TYPE_PAYMENT_SHEET VARCHAR(50),
        ID_ORGANIZATIONAL_UNIT UUID, -- ME FALTA LLAVE
        COMMENTARY VARCHAR(500),
        /*
        *   THESE FIELDS STORE ALL OF AN EMPLOYEE'S EARNINGS
        *   OVER A PERIOD OF TIME.
        */
        EMPLOYEES_TOTAL_SALARY NUMERIC(12, 4) DEFAULT 0.00,
        EMPLOYEES_TOTAL_EXTRA_HOURS NUMERIC(12, 4) DEFAULT 0.00,
        EMPLOYEES_TOTAL_EXTRA_SHIFT NUMERIC(12, 4) DEFAULT 0.00,
        EMPLOYEES_TOTAL_OTHER_INCOME NUMERIC(12, 4) DEFAULT 0.00,
        EMPLOYEES_TOTAL_VACATIONS NUMERIC(12, 4) DEFAULT 0.00,
        EMPLOYEES_TOTAL_HOLIDAY NUMERIC(12, 4) DEFAULT 0.00,
        EMPLOYEES_TOTAL_AGUINALDO NUMERIC(12, 4) DEFAULT 0.00,
        /*
        *   THESE FIELDS STORE ALL OF AN EMPLOYEE'S DISCOUNTS
        *   OVER A PERIOD OF TIME.
        */
        EMPLOYEES_TOTAL_ISSS NUMERIC(12, 4) DEFAULT 0.00,
        EMPLOYEES_TOTAL_AFP NUMERIC(12, 4) DEFAULT 0.00,
        EMPLOYEES_TOTAL_IPSFA NUMERIC(12, 4) DEFAULT 0.00,
        EMPLOYEES_TOTAL_ISR NUMERIC(12, 4) DEFAULT 0.00,
        EMPLOYEES_TOTAL_OTHER_DISCOUNTS NUMERIC(12, 4) DEFAULT 0.00,
        /*
        *   THESE FIELDS STORE AN EMPLOYER CONTRIBUTIONS OVER
        *   PERIOD OF TIME.
        */
        EMPLOYER_TOTAL_ISSS NUMERIC(12, 4) DEFAULT 0.00,
        EMPLOYER_TOTAL_AFP NUMERIC(12, 4) DEFAULT 0.00,
        EMPLOYER_TOTAL_IPSFA NUMERIC(12, 4) DEFAULT 0.00,
        EMPLOYER_TOTAL_INSAFORP NUMERIC(12, 4) DEFAULT 0.00,
        /*
        *   THESE FIELDS STORE INFORMATION ABOUT USER THAT 
        *   REGISTERED PAYMENT SHEET
        */
        REGISTERED_PAYMENT_SHEET BOOLEAN DEFAULT false,
        REGISTERED_PAYMENT_SHEET_DATE TIMESTAMP WITHOUT TIME ZONE,
        ID_USER_REGISTERED_PAYMENT_SHEET UUID,
        /*
        *   THESE FIELDS STORE INFORMATION ABOUT USER THAT
        *   CANCELED PAYMENT SHEET.
        */
        CANCELED_PAYMENT_SHEET BOOLEAN DEFAULT false,
        CANCELED_PAYMENT_SHEET_DATE TIMESTAMP WITHOUT TIME ZONE,
        ID_USER_CANCELED_PAYMENT_SHEET UUID,
		/*
		*   FIELDS TO CONDUCT AUDIT OF THE DATABASE
		*   THESE FIELDS ALLOW US TO KEEP CONTROL OF THE
		*   USERS WHO INTERACT WITH IT AND KNOW WHO
		*   ENTER OR UPDATE INFORMATION.
		*/
		ID_USER_CREATION UUID,
		ID_USER_UPDATE UUID,
		USER_BD VARCHAR(100) DEFAULT CURRENT_USER,
		CREATION_DATE TIMESTAMP WITHOUT TIME ZONE DEFAULT CURRENT_TIMESTAMP,
		UPDATE_DATE TIMESTAMP WITHOUT TIME ZONE
	)

-- Foreign key restriction for ID_USER_CREATION
ALTER TABLE HR.PAYMENT_SHEET
ADD CONSTRAINT FK_ID_USER_CREATION FOREIGN KEY (ID_USER_CREATION) REFERENCES GT.USERS(ID_USER) ON DELETE NO ACTION;

-- Foreign key restriction for ID_USER_UPDATE
ALTER TABLE HR.PAYMENT_SHEET
ADD CONSTRAINT FK_ID_USER_UPDATE FOREIGN KEY (ID_USER_UPDATE) REFERENCES GT.USERS(ID_USER) ON DELETE NO ACTION;

-- Foreign key restriction for ID_USER_CANCELED_PAYMENT_SHEET
ALTER TABLE HR.PAYMENT_SHEET
ADD CONSTRAINT FK_ID_USER_CANCELED FOREIGN KEY (ID_USER_CANCELED_PAYMENT_SHEET) REFERENCES GT.USERS(ID_USER) ON DELETE NO ACTION;

-- Foreign key restriction for ID_USER_REGISTERED_PAYMENT_SHEET
ALTER TABLE HR.PAYMENT_SHEET
ADD CONSTRAINT FK_ID_USER_REGISTERED FOREIGN KEY (ID_USER_REGISTERED_PAYMENT_SHEET) REFERENCES GT.USERS(ID_USER) ON DELETE NO ACTION;

-- Foreign key restriction for ID_ORGANIZATIONAL_UNIT
ALTER TABLE HR.PAYMENT_SHEET
ADD CONSTRAINT FK_ID_ORGANIZATIONAL_UNIT FOREIGN KEY (ID_ORGANIZATIONAL_UNIT) REFERENCES HR.ORGANIZATIONAL_UNIT(ID_ORGANIZATIONAL_UNIT) ON DELETE NO ACTION;
