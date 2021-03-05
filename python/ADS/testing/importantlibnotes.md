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

