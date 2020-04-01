# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['aws_iam_tester']

package_data = \
{'': ['*']}

install_requires = \
['boto3>=1.12.22,<2.0.0',
 'click>=7.1.1,<8.0.0',
 'pyyaml>=5.3,<6.0',
 'termcolor>=1.1.0,<2.0.0',
 'toml>=0.10.0,<0.11.0']

entry_points = \
{'console_scripts': ['aws-iam-tester = aws_iam_tester.cli:main']}

setup_kwargs = {
    'name': 'aws-iam-tester',
    'version': '0.1.2',
    'description': 'AWS IAM tester - simple command-line tool to check permissions handed out to IAM users and roles.',
    'long_description': '# Testing AWS IAM policies\n\n## Introduction\n\nAWS IAM policies are notouriously complex, it is too easy to add some unintended permissions and it is surprisingly difficult to identify these in heavily used AWS accounts.\n\nEven more surprisingly I couldn\'t find a ready-to-use utility that I could leverage.\n\nHence I created one myself.\n\n## Testing approach\n\nThe testing leverages AWS\' [IAM simulator (api)](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_testing-policies.html), that basically includes the same IAM evaluation logic that is applied when working in the console or using the cli. The beneits of this approach are:\n\n- It takes all different levels of policies into account. Think about permission boundaries, service control policies and so on.\n- It is an official service from AWS, so you can expect this to kept up to date over time.\n- The actual actions are evaluated, but NOT executed. Hence no need for cleaning up resources after testing.\n\n## Configuration\n\nIn order to run, a configuration of the tests to run is required.\n\nA sample configuration (with only one test) is shown, in various steps.\n\nFirst there is a global section where you define settings which are applied to all tests (unless overruled, more on that later).\n\n```yaml\n---\nuser_landing_account: 0123456789 # ID of AWS Account that is allowed to assume roles in the test account\nglobal_exemptions: # The roles and/or users below will be ignored in all tests. Regular expressions are supported\n- "^arn:aws:iam::(\\\\d{12}):user/(.*)(ADMIN|admin)(.*)$"\n- "^arn:aws:iam::(\\\\d{12}):role/(.*)(ADMIN|admin)(.*)$"\n- "^arn:aws:iam::(\\\\d{12}):role/AWSCloudFormationStackSetExecutionRole$"\n```\n\nThen you define a list of tests, each consisting at least of a set of:\n- actions\n- resources\n- the expected result (should it fail or succeed)\n\n```yaml\n# List of tests to execute. In general the configurations follow the rules of the AWS IAM Policy Simulator.\n# For more information: https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_testing-policies.html\ntests: \n- actions: # list of actions to validate\n  - "*:*"\n  - iam:*\n  - iam:AddUser*\n  - iam:Attach*\n  - iam:Create*\n  - iam:Delete*\n  - iam:Detach*\n  - iam:Pass*\n  - iam:Put*\n  - iam:Remove*\n  - iam:UpdateAccountPasswordPolicy\n  - sts:AssumeRole\n  - sts:AssumeRoleWithSAML\n  expected_result: fail # \'fail\' or \'succeed\'\n  resources: # list of resources to validate against\n  - "*"\n```\n\nRather than using all users and roles (without exemptions) you can also limit your test to a particular set of users and roles.\n\nThe test below does that, including defining a custom context that specifies multi factor authentication is disabled when running the test. By default the context under which the simulations are run assumes MFA is enabled, but you can override that with the `custom_context` element. For more information see the [AWS documentation](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_testing-policies.html).\n\n```yaml\n- actions: # Same list of actions, but now check (with a custom context) whether\n  - "*:*"\n  - iam:*\n  - iam:AddUser*\n  - iam:Attach*\n  - iam:Create*\n  - iam:Delete*\n  - iam:Detach*\n  - iam:Pass*\n  - iam:Put*\n  - iam:Remove*\n  - iam:UpdateAccountPasswordPolicy\n  - sts:AssumeRole\n  - sts:AssumeRoleWithSAML\n  expected_result: fail # \'fail\' or \'succeed\'\n  resources: # list of resources to validate against\n  - "*"\n  limit_to: # check this list for the admin users\n  - "^arn:aws:iam::(\\\\d*):user/(.*)(ADMIN|admin)(.*)$"\n  - "^arn:aws:iam::(\\\\d*):role/(.*)(ADMIN|admin)(.*)$"\n  # test if the admins are required to use multi factor authentication\n  custom_context: \n    - context_key_name: aws:MultiFactorAuthPresent\n      context_key_values: false\n      context_key_type: boolean\n```\n\nBelow an example where an additional set of roles is exempt from testing:\n\n```yaml\n- actions: # list of data centric actions\n  - redshift:GetClusterCredentials\n  - redshift:JoinGroup\n  - rds:Create*\n  - rds:Delete*\n  - rds:Modify*\n  - rds-db:connect\n  - s3:BypassGovernanceRetention\n  - s3:CreateBucket\n  - s3:DeleteBucket\n  - s3:DeleteBucketPolicy\n  - s3:PutBucketAcl\n  - s3:PutBucketPolicy\n  - s3:PutEncryptionConfiguration\n  - s3:ReplicateDelete\n  expected_result: fail # \'fail\' or \'succeed\'\n  resources: # list of resources to validate against\n  - "*"\n  exemptions: [\n  - "^arn:aws:iam::(\\\\d{12}):role/(.*)_worker$" # ignore this for the worker roles\n  ]\n```\n\nIf you want to run positive tests (i.e. tests that you need to succeed rather than fail), these `exemptions` don\'t work that well.\n\nIn that case you can limit your tests to a set of roles and users:\n\n```yaml\n- actions:\n  - s3:PutObject\n  expected_result: succeed\n  resources:\n  - "arn:aws:s3:::my_bucket/xyz/*"\n  limit_to: # if you specify this, test will only be performed for the sources below\n  - "^arn:aws:iam::(\\\\d{12}):role/my_worker$"\n```\n\n> Note that the exemptions are ignored when using a `limit_to` list.\n\n## How to use\n\nAssuming you have define a config.yml in your local directory, then to run and write the outputs to the local `./results` directory:\n\n```bash\naws-iam-tester --write-to-file\n```\n\nUsing a specific config file:\n\n```bash\naws-iam-tester --config-file my-config.yml\n```\n\nUsing a specific output location:\n\n```bash\naws-iam-tester --output-location /tmp\n```\n\nOr write to s3:\n\n```bash\naws-iam-tester --output-location s3://my-bucket/my-prefix\n```\n\nInclude only roles that can be assumed by human beings:\n\n```bash\naws-iam-tester --no-include-system-roles\n```\n\n> Note: including system roles does NOT include the aws service roles.\n\nOr print debug output:\n\n```bash\naws-iam-tester --debug\n```\n\nTo run a limited number of evaluations (which helps speeding things up, and avoiding API throttling issues):\n\n```bash\naws-iam-tester --number-of-runs 10\n```\n\nFor more information, run `aws-iam-tester --help` for more instructions.\n\n## Unit testing\n\n`pytest` is being used for testing the various options.\n\nAs long as the `aws-iam-tester` module is installed, you can run the [tests](./tests).\n\nAfter installing `tox`, you can also simply run `$ tox`.',
    'author': 'Gerco Grandia',
    'author_email': 'gerco.grandia@4synergy.nl',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/gercograndia/aws-iam-tester',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
