{#- -*- mode: sgml; tab-width: 1; indent-tabs-mode: nil -*-
 #
 # SPDX-License-Identifier: MIT
 # Copyright (c) 2022 MBition GmbH
-#}

{%- macro printMux(mux) %}
<MUX ID="{{mux.id}}">
  <SHORT-NAME>{{mux.short_name}}</SHORT-NAME>
  <LONG-NAME>{{mux.long_name|e}}</LONG-NAME>
  <BYTE-POSITION>{{mux.byte_position}}</BYTE-POSITION>
  <SWITCH-KEY>
    <BYTE-POSITION>{{mux.switch_key.byte_position}}</BYTE-POSITION>
    <BIT-POSITION>{{mux.switch_key.bit_position}}</BIT-POSITION>
    <DATA-OBJECT-PROP-REF ID-REF="{{mux.switch_key.dop_ref}}"/>
  </SWITCH-KEY>
  <DEFAULT-CASE>
    <SHORT-NAME>{{mux.default_case.short_name}}</SHORT-NAME>
    <LONG-NAME>{{mux.default_case.long_name}}</LONG-NAME>
    <STRUCTURE-REF ID-REF="{{mux.default_case.structure_ref}}"/>
  </DEFAULT-CASE>
  <CASES>
    {%- for case in mux.cases %}
    <CASE>
      <SHORT-NAME>{{case.short_name}}</SHORT-NAME>
      <LONG-NAME>{{case.long_name}}</LONG-NAME>
      <STRUCTURE-REF ID-REF="{{case.structure_ref}}"/>
      <LOWER-LIMIT>{{case.lower_limit}}</LOWER-LIMIT>
      <UPPER-LIMIT>{{case.upper_limit}}</UPPER-LIMIT>
    </CASE>
    {%- endfor %}
  </CASES>
</MUX>
{%- endmacro -%}
