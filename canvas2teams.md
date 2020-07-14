# canvas2teams

These are steps I followed to upload a list of students extracted from Canvas to a Microsoft Teams team using Powershell.

Note: If your course is in one of the programs supported by the RMIT College of Science, Engineering and Health (SEH), you may want to contact the Learning Enhancement Team, as they can provide more information on how to sync Canvas and Microsoft Teams: https://sites.rmit.edu.au/sister/2020/05/28/introducing-microsoft-teams/ 

## Extract List of Students from Canvas

On your course on Canvas:

1. Go to `Grades`
2. Click on `Actions -> Export`
   - This will download a `.csv` file with the list of students (and additional information such as the grades, which we will ignore)
3. Open the `.csv` with Excel or similar, and create a column `email`
   - Delete Row `2` (containing `Points Possible`)
   - Create a new column next at the right of column D (which contains `SIS Login ID`)
   - In Cell `E1`, add `email`
   - In Cell `E2`, add `=CONCAT(D2, “@student.rmit.edu.au”)`
   - Expand formula to cover the whole list of students
4. [Optional] Delete unnecessary columns (e.g., grades)
5. Save the changes
    - Hereafter, I will refer to this file as `YOUR_STUDENTS_LIST.csv`

Note: There is probably a better way to extract e-mails from students on Canvas (i.e., using Canvas API), but this is the method I used so far.

## Obtain Team's Group ID from Microsoft Teams

On Microsoft Teams:

1. Click on the `...` next to the Team title
2. Click on `Get link to team`
3. Copy the link to the team and grab the group ID form the URL

Hereafter I will refer to this ID as `YOUR_GROUP_ID`

## Import List of Students to the Team in Powershell

On Mac, install Powershell:

```
brew cask install powershell
```

On Mac, run Powershell:

```
pwsh
```

Install `MicrosoftTeams` Powershell module:

```
Install-Module -Name MicrosoftTeams
```

Connect and sign in:

```
Connect-MicrosoftTeams
```

Follow the instructions in the Powershell terminal, i.e:

```
WARNING: To sign in, use a web browser to open the page https://microsoft.com/devicelogin and enter the code YOU_WILL_SEE_THE_CODE_HERE to authenticate.
```

Double-check that your Group ID is correct:
```
Get-Team -groupId YOUR_GROUP_ID
```

Add students to the team by importing their e-mails:

```
Import-Csv YOUR_STUDENTS_LIST.csv | ForEach-Object {
   Add-TeamUser -GroupId YOUR_GROUP_ID -User $($_.email)
}
```

Note: If you get an error similar to this:
  ```
  Import-Csv: Cannot bind parameter 'Delimiter'. Cannot convert value "-\" to type "System.Char". Error: "String must be exactly one character long."
  ```
check that the characters in [the path of your file are correctly escaped for Powershell.](https://stackoverflow.com/questions/35225462/binding-delimiter-in-powershell)

Check users in your team:
```
Get-TeamUser -groupId YOUR_GROUP_ID
```
