
function createString(start, end) {
    const ONE_DAY = 86400000

    const options = { weekday: 'long', year: 'numeric', month: 'numeric', day: 'numeric' }

    const startdate = new Date(start)

    // date without time information -> full-day event
    if (start.length == 10) {
        const enddate = new Date(end) - ONE_DAY

        const start_str = startdate.toLocaleDateString('fi-FI', options)
        if (enddate - startdate > 0) {
            return start_str +  " - " + enddate.toLocaleDateString('fi-FI', options)
        }

        return start_str
    }

    const enddate = new Date(end)

    const start_str = startdate.toLocaleString('fi-FI', options) + ' - '

    if (enddate.getDate() > startdate.getDate() || enddate.getMonth() > startdate.getMonth() || ((enddate - startdate) > ONE_DAY)) {
        return start_str + enddate.toLocaleString('fi-FI', options)
    }
    
    return start_str + enddate.toLocaleTimeString('fi-FI', options)
}