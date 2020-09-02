import React, { useEffect, useState } from 'react';
import './styles.css';
import getSymbolFromCurrency from 'currency-symbol-map'
import CurrencyTextField from '@unicef/material-ui-currency-textfield'
import Button from '@material-ui/core/Button'
import { useHistory } from 'react-router-dom';
import api from '../../services/api'
import Table from '@material-ui/core/Table';
import TableBody from '@material-ui/core/TableBody';
import TableCell from '@material-ui/core/TableCell';
import TableContainer from '@material-ui/core/TableContainer';
import TableHead from '@material-ui/core/TableHead';
import TableRow from '@material-ui/core/TableRow';
import Paper from '@material-ui/core/Paper';
import { TextField, MenuItem } from '@material-ui/core';
import Pagination from '@material-ui/lab/Pagination';

export default function Main(){
    const [value, setValue] = useState('');
    const [amount, setAmount] = useState(0);
    const [currency, setCurrency] = useState('USD')
    const [currencyQuery, setCurrencyQuery] = useState('USD')
    const [queryLimit, setQueryLimit] = useState(1);
    const [currencyList, setCurrencyList] = useState(null)
    const [conversionHistory, setConversionHistory] = useState(null)
    const [page, setPage] = useState(1)
    const history = useHistory();


    const numberFormat = (value) =>
        new Intl.NumberFormat('en-IN', {
            style: 'decimal', minimumFractionDigits: "2", maximumFractionDigits: "2"
    }).format(value);

    const dateFormat = (value) => 
    new Intl.DateTimeFormat(
        'default',
        {
            year: 'numeric', month: 'numeric', day: 'numeric',
            hour: 'numeric', minute: 'numeric', second: 'numeric',
            hour12: false,
            timeZone: 'America/Los_Angeles' 
        }
    ).format(value)

    async function saveCurrency(currency, amount){
        const data = {
            currency,
            amount
        };
        try {
            await api.post('currency-transaction', data);
            loadHistory();
            setAmount(0);
            history.push('/');
        } catch (err) {
            alert('Erro no cadastro, tente novamente mais tarde');
        }
    }

    async function loadHistory(){
        try {
            const response = await api.get("currency-transactions/last?limit=".concat(queryLimit > 0 ? queryLimit : 1).concat(currencyQuery!== ""  ? "&currency=" + currencyQuery : "").concat("&page=".concat(page)));
            const parsed_response = await response.data;
            setConversionHistory(parsed_response);
        } catch (err) {
            console.log(err)
            alert('Erro no cadastro, tente novamente mais tarde');
        }
    }
    
    const handleCurrencySelect = (event) => {
        setCurrency(event.target.value)
    };
 
    const handleSetAmount = (_, value) => {
        setAmount(value);
    }

    useEffect(() => {
        (async () => {
            if (currencyList == null){
                const response = await api.get('/get-forecast');
                const parsed_response = await response.data;
                setCurrencyList(parsed_response);
            }
          })();
        loadHistory();
    }, [page]);


    return (
        
        <div className="main-container">
            <div className="saving-container">
                <div className="currencySelect">
                <TextField
                    select
                    variant="outlined"
                    label="Currency"
                    value={currency}
                    onChange={handleCurrencySelect}
                >
                    <MenuItem value="">
                    <em>None</em>
                    </MenuItem>
                    {currencyList != null ? (
                            Object.keys(currencyList).map(
                                value => (
                                    <MenuItem value={value}>{value}</MenuItem>
                                )
                            )
                          ) : <p></p>
                    }
                </TextField>
                </div>
                <div className="amount">
                    <CurrencyTextField  label="Amount" variant="outlined" value={value} 
                                        decimalPlacesShownOnFocus="8" decimalPlacesShownOnBlur="2"
                                        currencySymbol={getSymbolFromCurrency(currency)} outputFormat="string"
                                        onChange={handleSetAmount}/>
                </div>
                    
                <div className="finalAmount">
                    <CurrencyTextField  label="Final value" variant="outlined" readOnly={true} value={currencyList != null ? amount * currencyList[currency] : 0} 
                                        decimalPlacesShownOnFocus="8" decimalPlacesShownOnBlur="2"
                                        currencySymbol={getSymbolFromCurrency("USD")} outputFormat="string" 
                                    />
                </div>
                <div className="save-button"> 
                    <Button variant="contained" onClick={() => saveCurrency(currency, amount)}>Save</Button>
                </div>
            </div> 

            <div className="data-list">
                <div className="selectors">
                    <div className="currencyQuery">
                        <TextField
                            select                    
                            variant="outlined"
                            label="Currency"
                            value={currencyQuery}
                            onChange={(e) => (setCurrencyQuery(e.target.value))}
                        >
                            <MenuItem value="">
                            <em>None</em>
                            </MenuItem>
                            {currencyList != null ? (
                                    Object.keys(currencyList).map(
                                        value => (
                                            <MenuItem value={value}>{value}</MenuItem>
                                        )
                                    )
                                ) : <p></p>
                            }
                        </TextField>
                    </div>
                    <div className="registriesQuery">
                        <TextField variant="outlined" label="Registries" type="number" onChange={(e) => {setQueryLimit(e.target.value)}}></TextField>  
                    </div>
                    
                    <div className="search-button"> 
                        
                        <Button variant="contained" onClick={loadHistory}>Refresh</Button>
                    </div>
                </div>
                <div className="table">
                    <TableContainer component={Paper}>
            
                        <Table aria-label="simple table">
                            <TableHead>
                            <TableRow>
                                <TableCell>Currency</TableCell>
                                <TableCell align="right">Amount</TableCell>
                                <TableCell align="right">Rate</TableCell>
                                <TableCell align="right">Total Amount USD</TableCell>
                                <TableCell align="right">Date</TableCell>
                            </TableRow>
                            </TableHead>
                            <TableBody>
                                {
                                    conversionHistory != null ? (
                                    conversionHistory['data'].map((row) => (
                                        <TableRow key={row.id}>
                                        <TableCell component="th" scope="row">{row.transactionCurrencySymbol}</TableCell>
                                        <TableCell align="right">{numberFormat(row.transactionAmount)}</TableCell>
                                        <TableCell align="right">{numberFormat(row.currencyRate)}</TableCell>
                                        <TableCell align="right">{numberFormat(row.finalAmount)}</TableCell>
                                        <TableCell align="right">{dateFormat(Date.parse(row.transactionDateTime))}</TableCell>
                                        </TableRow>
                                    ))
                                    ):(
                                        <TableRow >
                                        </TableRow>
                                    )
                                } 
                            </TableBody>
                        </Table>
                    </TableContainer>
                </div>
                <div className="pagination-wrapper">
                    <Pagination className="pagination" onChange={(_, page) => (setPage(page))} count={conversionHistory !== null ? conversionHistory.pages : 1} shape="rounded" />
                </div>
            </div>
        </div>
    );
}