# Important notes to the pyads/ads.py library:

Find out what the *read-state(self)* numbers mean:
```py
    def read_state(self) -> Optional[Tuple[int, int]]:
        """Read the current ADS-state and the machine-state.

        Read the current ADS-state and the machine-state from the ADS-server.

        :rtype: (int, int)
        :return: adsState, deviceState

        """
        if self._port is not None:
            return adsSyncReadStateReqEx(self._port, self._adr)

        return None
```

Read up on write_control():
```py
    def write_control(
        self, ads_state: int, device_state: int, data: Any, plc_datatype: Type
    ) -> None:
        """Change the ADS state and the machine-state of the ADS-server.

        :param int ads_state: new ADS-state, according to ADSTATE constants
        :param int device_state: new machine-state
        :param data: additional data
        :param int plc_datatype: datatype, according to PLCTYPE constants

        :note: Despite changing the ADS-state and the machine-state it is
            possible to send additional data to the ADS-server. For current
            ADS-devices additional data is not progressed.
            Every ADS-device is able to communicate its current state to other
            devices. There is a difference between the device-state and the
            state of the ADS-interface (AdsState). The possible states of an
            ADS-interface are defined in the ADS-specification.

        """
        if self._port is not None:
            return adsSyncWriteControlReqEx(
                self._port, self._adr, ads_state, device_state, data, plc_datatype
            )
```

Remember read_device_info(self);
```py
    def read_device_info(self) -> Optional[Tuple[str, AdsVersion]]:
        """Read the name and the version number of the ADS-server.

        :rtype: string, AdsVersion
        :return: device name, version

        """
        if self._port is not None:
            return adsSyncReadDeviceInfoReqEx(self._port, self._adr)

        return None
```

Read up on def get_all_symbols(self) -> List[AdsSymbol]: line741

Double check this, might be useful for testing and reading lists.
```py
def read_list_by_name(
        self,
        data_names: List[str],
        cache_symbol_info: bool = True,
        ads_sub_commands: int = MAX_ADS_SUB_COMMANDS,
        structure_defs: Optional[Dict[str, StructureDef]] = None,
    ) -> Dict[str, Any]:
        """Read a list of variables.

        Will split the read into multiple ADS calls in chunks of ads_sub_commands by default.

        MAX_ADS_SUB_COMMANDS comes from Beckhoff recommendation:
        https://infosys.beckhoff.com/english.php?content=../content/1033/tc3_adsdll2/9007199379576075.html&id=9180083787138954512

        :param data_names: list of variable names to be read
        :type data_names: list[str]
        :param bool cache_symbol_info: when True, symbol info will be cached for future reading
        :param int ads_sub_commands: Max number of ADS-Sub commands used to read the variables in a single ADS call.
            A larger number can be used but may jitter the PLC execution!
        :param dict structure_defs: for structured variables, optional mapping of
            data name to special tuple defining the structure and
            types contained within it according to PLCTYPE constants

        :return adsSumRead: A dictionary containing variable names from data_names as keys and values read from PLC for each variable
        :rtype dict(str, Any)

        """
        if cache_symbol_info:
            new_items = [i for i in data_names if i not in self._symbol_info_cache]
            new_cache = {
                i: adsGetSymbolInfo(self._port, self._adr, i) for i in new_items
            }
            self._symbol_info_cache.update(new_cache)
            data_symbols = {i: self._symbol_info_cache[i] for i in data_names}
        else:
            data_symbols = {
                i: adsGetSymbolInfo(self._port, self._adr, i) for i in data_names
            }

        structure_defs = structure_defs or {}
        def sum_read(port, adr, data_names, data_symbols):
            result = adsSumRead(port, adr, data_names, data_symbols,
                                list(structure_defs.keys()))

            for data_name, structure_def in structure_defs.items():
                result[data_name] = dict_from_bytes(result[data_name], structure_def)

            return result

        if len(data_names) <= ads_sub_commands:
            return sum_read(self._port, self._adr, data_names, data_symbols)

        return_data: Dict[str, Any] = {}
        for data_names_slice in _list_slice_generator(data_names, ads_sub_commands):
            return_data.update(
                sum_read(self._port, self._adr, data_names_slice, data_symbols)
            )
        return return_data
```

