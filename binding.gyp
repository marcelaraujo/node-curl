{
  'targets': [
    {
      'target_name': 'node-curl',
      'cflags': ['-Wall', '-O1', '-fno-inline-functions'],
      'cflags_cc': ['-Wall', '-O1', '-fno-inline-functions'],
      'sources': ['src/node-curl.cc'],
      'libraries': ['-lcurl']
    }
  ]
}
