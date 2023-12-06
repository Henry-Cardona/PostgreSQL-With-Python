
CREATE TABLE
	GT.DEPARTMENT (
		/*
        *   UNIQUE FILDS
        */
		ID_DEPARTMENT UUID DEFAULT uuid_generate_v4 () PRIMARY KEY,
		DEPARTMENT_CODE INTEGER UNIQUE,
		DEPARTMENT_NAME VARCHAR(100),
		/*
		*	FIELDS TO CONDUCT AUDIT OF THE DATABASE
		*	THESE FIELDS ALLOW US TO KEEP CONTROL OF THE
		*	USERS WHO INTERACT WITH IT AND KNOW WHO
		*	ENTER OR UPDATE INFORMATION.
		*/
		ID_USER_CREATION UUID,
		ID_USER_UPDATE UUID,
		USER_BD VARCHAR(100) DEFAULT CURRENT_USER,
		CREATION_DATE TIMESTAMP WITHOUT TIME ZONE DEFAULT CURRENT_TIMESTAMP,
		UPDATE_DATE TIMESTAMP WITHOUT TIME ZONE
	)

-- Foreign key restriction for ID_USER_CREATION
ALTER TABLE GT.DEPARTMENT
ADD CONSTRAINT FK_ID_USER_CREATION FOREIGN KEY (ID_USER_CREATION) REFERENCES GT.USERS(ID_USER) ON DELETE NO ACTION;

-- Foreign key restriction for ID_USER_UPDATE
ALTER TABLE GT.DEPARTMENT
ADD CONSTRAINT FK_ID_USER_UPDATE FOREIGN KEY (ID_USER_UPDATE) REFERENCES GT.USERS(ID_USER) ON DELETE NO ACTION;
