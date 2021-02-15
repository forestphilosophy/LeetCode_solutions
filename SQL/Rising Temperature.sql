SELECT Yesterday.id
FROM Weather
INNER JOIN
    (SELECT id,DATEADD(day, -1, recordDate) AS YesterdayDate,Temperature
    FROM Weather) AS Yesterday
ON Weather.recordDate = Yesterday.YesterdayDate
WHERE Yesterday.Temperature > Weather.Temperature
