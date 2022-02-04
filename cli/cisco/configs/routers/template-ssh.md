<!-- Configuring ssh access to a cisco router -->

<!--- Step 1: Configure the hostname if you have not previously done so.-->

hostname *hostname*

<!--- The aaa new-model command causes the local username and password on the router -->
<!--- to be used in the absence of other AAA statements. -->
<!--- Instead of aaa new-model, you can use the login local command. -->

aaa new-model
username *username* *privilege [0-15]* secret *password*

<!--- Step 2: Configure the DNS domain of the router. -->

ip domain-name rtp.cisco.com

<!--- Step 3: Generate an SSH key to be used with SSH. Best practice is 2048 bits -->

crypto key generate rsa
2048

<!--- Step 4: By default the vty transport is Telnet. In this case, -->
<!--- Telnet is disabled and only SSH is supported. -->

line vty 0 4
transport input SSH

<!-- Step 5: enable version 2-->
ssh version 2