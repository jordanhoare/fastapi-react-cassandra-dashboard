import PropTypes from 'prop-types';
import { useState } from 'react';
import { Link as RouterLink } from 'react-router-dom';
import { Box, Link, Table, TableBody, TableCell, TableContainer, TableHead, TableRow } from '@mui/material';
import NumberFormat from 'react-number-format';


function descendingComparator(a, b, orderBy) {
    if (b[orderBy] < a[orderBy]) {
        return -1;
    }
    if (b[orderBy] > a[orderBy]) {
        return 1;
    }
    return 0;
}

function getComparator(order, orderBy) {
    return order === 'desc' ? (a, b) => descendingComparator(a, b, orderBy) : (a, b) => -descendingComparator(a, b, orderBy);
}

function stableSort(array, comparator) {
    const stabilizedThis = array.map((el, index) => [el, index]);
    stabilizedThis.sort((a, b) => {
        const order = comparator(a[0], b[0]);
        if (order !== 0) {
            return order;
        }
        return a[1] - b[1];
    });
    return stabilizedThis.map((el) => el[0]);
}

// ==============================|| ORDER TABLE - HEADER CELL ||============================== //

const headCells = [
    {
        id: 'registration_number',
        align: 'left', 
        disablePadding: false,
        label: 'Registration'
    },
    {
        id: 'car_make',
        align: 'left', 
        disablePadding: false,
        label: 'Make'
    },
    {
        id: 'car_model',
        align: 'left',
        disablePadding: true,
        label: 'Model'
    },
    {
        id: 'car_category',
        align: 'left',
        disablePadding: true,
        label: 'Body Type'
    },
    {
        id: 'rental_start_time',
        align: 'left',
        disablePadding: true,
        label: 'Rental Start'
    },
    {
        id: 'rental_end_time',
        align: 'left',
        disablePadding: true,
        label: 'Rental End'
    },
];



// ==============================|| ORDER TABLE - HEADER ||============================== //

function OrderTableHead({ order, orderBy }) {
    return (
        <TableHead>
            <TableRow>
                {headCells.map((headCell) => (
                    <TableCell
                        key={headCell.id}
                        align={headCell.align}
                        padding={headCell.disablePadding ? 'none' : 'normal'}
                        sortDirection={orderBy === headCell.id ? order : false}
                    >
                        {headCell.label}
                    </TableCell>
                ))}
            </TableRow>
        </TableHead>
    );
}

OrderTableHead.propTypes = {
    order: PropTypes.string,
    orderBy: PropTypes.string
};


// ==============================|| ORDER TABLE ||============================== //

export default function OrdersTable( {cars} ) {
    const [order] = useState('asc');
    const [orderBy] = useState('registration_number');
    const [selected] = useState([]);

    const isSelected = (registration_number) => selected.indexOf(registration_number) !== -1;

    return (
        <Box>
            <TableContainer
                sx={{
                    width: '100%',
                    overflowX: 'auto',
                    position: 'relative',
                    display: 'block',
                    maxWidth: '100%',
                    '& td, & th': { whiteSpace: 'nowrap' }
                }}
            >
                <Table
                    aria-labelledby="tableTitle"
                    sx={{
                        '& .MuiTableCell-root:first-child': {
                            pl: 2
                        },
                        '& .MuiTableCell-root:last-child': {
                            pr: 3
                        }
                    }}
                >
                    <OrderTableHead order={order} orderBy={orderBy} />
                    <TableBody>
                        {stableSort(cars, getComparator(order, orderBy)).map((car, index) => {
                            const isItemSelected = isSelected(car.registration_number);
                            const labelId = `enhanced-table-checkbox-${index}`;

                            return (
                                <TableRow
                                    hover
                                    role="checkbox"
                                    sx={{ '&:last-child td, &:last-child th': { border: 0 } }}
                                    aria-checked={isItemSelected}
                                    tabIndex={-1}
                                    key={car.registration_number}
                                    selected={isItemSelected}
                                >
                                    <TableCell component="th" id={labelId} scope="row" align="left">
                                        <Link color="secondary" component={RouterLink} to="">
                                            {car.registration_number}
                                        </Link>
                                    </TableCell>
                                    <TableCell align="left">{car.car_make}</TableCell>
                                    <TableCell align="left">{car.car_model}</TableCell>
                                    <TableCell align="left">{car.car_category}</TableCell>
                                    <TableCell align="left">
                                        <NumberFormat value={car.rental_start_time} displayType="text" />
                                    </TableCell>
                                    <TableCell align="left">
                                        <NumberFormat value={car.rental_end_time} displayType="text" />
                                    </TableCell>
                                </TableRow>
                            );
                        })}
                    </TableBody>
                </Table>
            </TableContainer>
        </Box>
    );
}
